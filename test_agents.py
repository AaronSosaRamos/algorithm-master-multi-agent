from agents.agents import compile_agents
from phi.agent import RunResponse
from phi.utils.pprint import pprint_run_response

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

if __name__ == "__main__":
    urls = ["https://cusack.hope.edu/Notes/Notes/Algorithms/BFSandDFS.pdf"]

    agent_team = compile_agents(urls)

    response: RunResponse = agent_team.run("""
    Analyse in details the DFS and BFS algorithms for graphs. Return the results in JSON.
    """)
    
    pprint_run_response(response, markdown=True)

    print(f"Content: {response.content}")
    print(f"Conten Type: {response.content_type}")