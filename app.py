import streamlit
import plotly.express as px
import pandas

def process_query(query):
    return query

def display_map(lat, lon):
    streamlit.plotly_chart(
        plotly.scatter_mapbox(
            pandas.DataFrame({
                'lat': [lat],
                'lon': [lon],
                'name': ['Location']
            }),
            lat='lat',
            lon='lon',
            hover_name='name',
            zoom=10,
            height=600,
            width=800
        )
    )

def main():
    streamlit.set_page_config( page_title="Voltient", page_icon="⚡️")
    streamlit.title("⚡️ Voltient")
    streamlit.write("""
    Voltient helps you find optimal locations for your data center by leveraging international data for
    - Power plant capacity and sources
    - Climate change projections
    - Water avaliability
    - Real estate and regulatory frameworks
             """)

    if "messages" not in streamlit.session_state:
        streamlit.session_state.messages = []
    for message in streamlit.session_state.messages:
        with streamlit.chat_message(message["role"]):
            streamlit.write(message["content"])

    user_input = streamlit.chat_input("Location for 50MW nuclear-powered edge data center in Asia-Pacific...")

    if user_input:
        streamlit.session_state.messages.append({"role": "user", "content": user_input})
        streamlit.session_state.messages.append({"role": "assistant", "content": process_query(user_input)})
        streamlit.rerun()
    
    display_map(40.7128, 74.0060)
    
  
if __name__ == "__main__":
    main()
