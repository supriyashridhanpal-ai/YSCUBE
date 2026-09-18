from app.graph import StudyGraph
from app.agent import Atlas


DATA_DIR = "data"


def main():
    print("===================================")
    print("       ATLAS AGENT AI")
    print(" Clinical Trial Intelligence Agent")
    print("===================================")

    graph = StudyGraph(DATA_DIR)

    print("\nBuilding Study Knowledge Graph...")
    graph.build()

    print("Loaded tables:")
    for table in graph.data:
        print(f" - {table}")

    agent = Atlas(graph)

    print("\nATLAS is ready.")
    print("Type 'exit' to stop.\n")

    while True:
        question = input("You: ")

        if question.lower() == "exit":
            break

        result = agent.answer(question)

        print("\nATLAS:")
        print(result["answer"])
        print(f"Confidence: {result['confidence']}")
        print(f"Evidence: {result['evidence']}")
        print()


if __name__ == "__main__":
    main()
