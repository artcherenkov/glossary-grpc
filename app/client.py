import grpc
from google.protobuf import empty_pb2

import glossary_pb2
import glossary_pb2_grpc

def run():
    with grpc.insecure_channel('127.0.0.1:50052') as channel:
        stub = glossary_pb2_grpc.GlossaryServiceStub(channel)

        # Пример: создать термин
        create_resp = stub.CreateTerm(glossary_pb2.CreateOrUpdateTermRequest(
            term=glossary_pb2.Term(key="python", description="Язык программирования")
        ))
        print("CreateTerm:", create_resp)

        # Пример: получить термин
        get_resp = stub.GetTerm(glossary_pb2.TermKeyRequest(key="python"))
        print("GetTerm:", get_resp)

        # Пример: обновить термин
        update_resp = stub.UpdateTerm(glossary_pb2.CreateOrUpdateTermRequest(
            term=glossary_pb2.Term(key="python", description="Высокоуровневый язык")
        ))
        print("UpdateTerm:", update_resp)

        # Пример: получить список
        list_resp = stub.ListTerms(empty_pb2.Empty())
        print("ListTerms:", list_resp)

        # Пример: удалить термин
        stub.DeleteTerm(glossary_pb2.TermKeyRequest(key="python"))
        print("Термин 'python' удалён.")

if __name__ == "__main__":
    run()
