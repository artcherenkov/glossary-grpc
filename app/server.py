import grpc
from concurrent import futures
from google.protobuf import empty_pb2
from grpc_reflection.v1alpha import reflection

# Локальные модули
from .database import Base, engine, SessionLocal
from . import crud

import glossary_pb2
import glossary_pb2_grpc

# Создаём таблицы, если их нет
Base.metadata.create_all(bind=engine)


class GlossaryServiceServicer(glossary_pb2_grpc.GlossaryServiceServicer):
    def CreateTerm(self, request, context):
        with SessionLocal() as db:
            existing = crud.get_term(db, request.term.key)
            if existing:
                context.set_code(grpc.StatusCode.ALREADY_EXISTS)
                context.set_details("Term already exists")
                return glossary_pb2.TermResponse()

            created = crud.create_term(db, request.term.key, request.term.description)
            return glossary_pb2.TermResponse(
                term=glossary_pb2.Term(
                    key=created.key,
                    description=created.description
                )
            )

    def GetTerm(self, request, context):
        with SessionLocal() as db:
            term_obj = crud.get_term(db, request.key)
            if not term_obj:
                context.set_code(grpc.StatusCode.NOT_FOUND)
                context.set_details("Term not found")
                return glossary_pb2.TermResponse()

            return glossary_pb2.TermResponse(
                term=glossary_pb2.Term(
                    key=term_obj.key,
                    description=term_obj.description
                )
            )

    def UpdateTerm(self, request, context):
        with SessionLocal() as db:
            existing = crud.get_term(db, request.term.key)
            if not existing:
                context.set_code(grpc.StatusCode.NOT_FOUND)
                context.set_details("Term not found")
                return glossary_pb2.TermResponse()

            updated = crud.update_term(db, existing.key, request.term.description)
            return glossary_pb2.TermResponse(
                term=glossary_pb2.Term(
                    key=updated.key,
                    description=updated.description
                )
            )

    def DeleteTerm(self, request, context):
        with SessionLocal() as db:
            success = crud.delete_term(db, request.key)
            if not success:
                context.set_code(grpc.StatusCode.NOT_FOUND)
                context.set_details("Term not found")
            return empty_pb2.Empty()

    def ListTerms(self, request, context):
        with SessionLocal() as db:
            terms_list = crud.list_terms(db)
            terms_proto = [
                glossary_pb2.Term(key=t.key, description=t.description)
                for t in terms_list
            ]
            return glossary_pb2.TermsListResponse(terms=terms_proto)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    glossary_pb2_grpc.add_GlossaryServiceServicer_to_server(GlossaryServiceServicer(), server)

    # Включаем рефлексию
    SERVICE_NAMES = (
        glossary_pb2.DESCRIPTOR.services_by_name['GlossaryService'].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)

    server.add_insecure_port('[::]:50052')
    server.start()
    print("gRPC сервер запущен на порту 50052. Йо-хо-хо!")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
