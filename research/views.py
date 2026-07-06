from django.shortcuts import render
from research.services.workflow_service import run_workflow


def home(request):
    return render(request, "home.html")


def generate_report(request):

    if request.method == "POST":

        query = request.POST.get("query")

        doc_format = request.POST.get("doc_format")

        result = run_workflow(query, doc_format)

        context = {

            "summary": result.get("summary_data"),

            "output": result.get("final_output")

        }

        return render(request, "result.html", context)

    return render(request, "home.html")