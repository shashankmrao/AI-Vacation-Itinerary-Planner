from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.AI_Trip_Planner.agent.agentic_workflow import GraphBuilder
from src.AI_Trip_Planner.utils.save_to_document import save_document
from starlette.responses import JSONResponse
import os
import datetime
from dotenv import load_dotenv
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryRequest(BaseModel):
    question: str

@app.post("/query")
async def query_travel_agent(query: QueryRequest):
    try:
        print(query)
        graph = GraphBuilder(model_provider = "groq")
        react_app = graph()

        png_graph = react_graph.get_graph().draw_mermaid_png()
        with open("my_graph.png", "wb") as f:
            f.write(png_graph)

        print(f"Graph saved as 'my_graph.png' in {os.getcwd()}")

        messages={"messages": [query.question]}
        output=react_app.invoke(messages)

        if isinstance(output, dict) and "messages" in output:
            final_output = output["messages"][-1].content
        else:
            final_output = str(output)

        save_document(final_output)

        return {"answer": final_output}
    except Exception as e:
        print(f"Error processing query: {e}")
        return JSONResponse(status_code=500, content={"error": str(e)})
