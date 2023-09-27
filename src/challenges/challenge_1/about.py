import streamlit as st

def main():
    # sidebar menu
    with st.sidebar:
        
        st.info("About the project")
        
        st.markdown("---")
        
        st.markdown(" # DTE DATATHON")
        
        st.markdown("""This is in fulfillment of the dte consultancy datathon that required the participants to investigate the 
                    trends and patterns of urbanization in Kenya using open-source data. The submission by this team considers
                    socio-economic factors such as GDP, population growth, agriculture, infrastructure and employment opportunities""")
        
        st.markdown("""The data used in this dashboard is just a basic look into the urbanization trends in Kenya.""")
        
        st.markdown("## The team")
        
        st.markdown('''The project was undertaken by Getrude Obwoge and Teofilo Ligawa''')
        
        st.info("")
        
if __name__ == '__main__':
    main()