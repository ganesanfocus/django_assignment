from research.workflow.graph import app


def run_workflow(query, doc_format):

    state = {
        "query": query,
        "requires_doc": True,
        "doc_format": doc_format,
        "research_data": "",
        "summary_data": "",
        "final_output": ""
    }

    result = app.invoke(state)

    return result