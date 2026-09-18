from app.graph import StudyGraph


def test_graph_creation():
    graph = StudyGraph("data")

    assert graph is not None
    assert graph.data == {}
