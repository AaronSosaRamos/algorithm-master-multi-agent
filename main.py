from agents.agents import compile_agents
from phi.agent import RunResponse
from phi.utils.pprint import pprint_run_response
import gradio as gr

def process_query(query, urls):
    """
    Process the user input query and list of URLs to analyze DFS and BFS algorithms.
    """
    # Convert the comma-separated URLs into a list
    url_list = [url.strip() for url in urls.split(",")]

    # Compile the agents using the provided URLs
    try:
        agent_team = compile_agents(url_list)
    except Exception as e:
        return f"Error in compiling agents: {str(e)}"

    # Run the query using the agent team
    try:
        response: RunResponse = agent_team.run(query)
    except Exception as e:
        return f"Error during agent execution: {str(e)}"

    # Pretty print and format the response
    pprint_run_response(response, markdown=True)
    return response.content

if __name__ == '__main__':
    # Create the Gradio interface
    with gr.Blocks() as demo:
        gr.Markdown("# Algorithm Master Multi Agent System")
        gr.Markdown("Enter your query and a list of URLs (separated by commas) below:")
        
        with gr.Row():
            query_input = gr.Textbox(label="Query", placeholder="Enter your query here", lines=3)
            urls_input = gr.Textbox(label="URLs", placeholder="Enter URLs separated by commas", lines=2)
        
        output = gr.Textbox(label="Analysis Results", placeholder="Results will appear here", lines=10, interactive=False)
        submit_button = gr.Button("Analyze")

        submit_button.click(
            process_query, 
            inputs=[query_input, urls_input], 
            outputs=output
        )

    # Launch the Gradio app
    demo.launch()
