# # imports
# import streamlit as st
# import requests
# from myapp import recommender


# # Base URL for your FastAPI server
# #API_URL = "http://127.0.0.1:8000"
# API_URL = "http://backend:8000" #when using docker

# st.title("Movie Recommender")

# # Input for movie name and transform to lowercase
# movie_input = st.selectbox(label="Select a Movie", index=None,
#                            options=recommender.get_movies_list(),
#                            help="Select a movie to get recommendations") 

# if movie_input:
#     movie_input = movie_input.lower()

# # If user clicks "Get Recommendations"
# if st.button("Get Recommendations"):
#     # And movie name is not empty
#     if movie_input:
#         # Call the /recommend/ endpoint
#         response = requests.get(f"{API_URL}/recommend/", params={"movie": movie_input})
        
#         # If the response is successful
#         if response.status_code == 200:
#             # Get the JSON response
#             data = response.json()
            
#             # Display the movie and recommendations. If recs not found, return empty list
#             recs = data.get("recommendations", [])
            
#             # Write recommendations. For each recommendation, display title and movie_id
#             st.write("### Recommendations:")

#             # Enumerate to get recommendation number, movie ID, and title
#             hashmap = {n:{"movie_id": rec["movie_id"], "title": rec["title"]} for n, rec in enumerate(recs, start=1)}
            
#             # Create columns
#             col1, col2, col3, col4 = st.columns(4)

#             with col1:
#                 # Choose a recommended movie
#                 st.write(str.capitalize(hashmap[1]["title"]))
#                 # Button to register a click for the recommendation
#                 def click_response(): 
#                     click_response = requests.post(f"{API_URL}/click/", params={"movie_id": hashmap[1]["movie_id"]})
#                     if click_response.status_code == 200:
#                         st.success(f"Registered click for {hashmap[1]['title']}")
#                 # If clicked, add a click to counter
#                 if st.button(label=hashmap[1]["movie_id"], on_click=click_response):
#                     pass

#                 # Click percentage
#                 # Fetch and display the click percentage
#                 stats_response = requests.get(f"{API_URL}/click_stats/", params={"movie_id": hashmap[1]["movie_id"]})
#                 if stats_response.status_code == 200:
#                     stats = stats_response.json()
#                     click_percentage = stats.get("click_percentage", 0)
#                     st.write(f"Click Rate: {click_percentage:.1f}%")

            
#             with col2:
#                 #Choose movie 2
#                 st.write(str.capitalize(hashmap[2]["title"]))
#                 # Button to register a click for the recommendation
#                 def click_response(): 
#                     click_response = requests.post(f"{API_URL}/click/", params={"movie_id": hashmap[2]["movie_id"]})
#                     if click_response.status_code == 200:
#                         st.success(f"Registered click for {hashmap[2]['title']}")
#                 # If clicked, add a click to counter
#                 if st.button(label=hashmap[2]["movie_id"], on_click=click_response):
#                     pass

#                 # Click percentage
#                 # Fetch and display the click percentage
#                 stats_response = requests.get(f"{API_URL}/click_stats/", params={"movie_id": hashmap[2]["movie_id"]})
#                 if stats_response.status_code == 200:
#                     stats = stats_response.json()
#                     click_percentage = stats.get("click_percentage", 0)
#                     st.write(f"Click Rate: {click_percentage:.1f}%")


                
#             with col3:
#                 # 3
#                 st.write(str.capitalize(hashmap[3]["title"]))
#                 # Button to register a click for the recommendation
#                 def click_response(): 
#                     click_response = requests.post(f"{API_URL}/click/", params={"movie_id": hashmap[3]["movie_id"]})
#                     if click_response.status_code == 200:
#                         st.success(f"Registered click for {hashmap[3]['title']}")
#                 # If clicked, add a click to counter
#                 if st.button(label=hashmap[3]["movie_id"], on_click=click_response):
#                     pass
                
#                 # Click percentage
#                 # Fetch and display the click percentage
#                 stats_response = requests.get(f"{API_URL}/click_stats/", params={"movie_id": hashmap[3]["movie_id"]})
#                 if stats_response.status_code == 200:
#                     stats = stats_response.json()
#                     click_percentage = stats.get("click_percentage", 0)
#                     st.write(f"Click Rate: {click_percentage:.1f}%")

#             with col4:
#                 #4
#                 st.write(str.capitalize(hashmap[4]["title"]))
#                 # Button to register a click for the recommendation
#                 def click_response(): 
#                     click_response = requests.post(f"{API_URL}/click/", params={"movie_id": hashmap[4]["movie_id"]})
#                     if click_response.status_code == 200:
#                         st.success(f"Registered click for {hashmap[4]['title']}")
#                 # If clicked, add a click to counter
#                 if st.button(label=hashmap[4]["movie_id"], on_click=click_response):
#                     pass

#                 # Click percentage
#                 # Fetch and display the click percentage
#                 stats_response = requests.get(f"{API_URL}/click_stats/", params={"movie_id": hashmap[4]["movie_id"]})
#                 if stats_response.status_code == 200:
#                     stats = stats_response.json()
#                     click_percentage = stats.get("click_percentage", 0)
#                     st.write(f"Click Rate: {click_percentage:.1f}%")

                      
            
#         else:
#             st.error("Movie not listed. Please try again.")
#     else:
#         st.warning("Please enter a movie name.")

# # sidepanel
# with st.sidebar:
#     st.title("Add a New Movie to the Database")
    
#     # Input for movie name and transform to lowercase
#     new_movie = st.text_input("New Movie name:")
#     if new_movie:
#         new_movie = str.lower(new_movie)
#     new_category = st.selectbox(index=None, label="New Movie Category", help="Select the movie category",
#                                   options=["Action", "Adventure", "Animation", "Children", "Comedy", "Crime", "Documentary",
#                                             "Drama", "Fantasy", "Film-Noir", "Horror", "Musical", "Mystery", "Romance",
#                                             "Sci-Fi", "Thriller", "War", "Western"])
#     if new_category:
#         new_category = str.lower(new_category)

#     new_release_dt = st.text_input("Release Date DD-Mth-YYYY", value='01-Jan-2000')
#     new_rating = st.number_input("Rating", min_value=1.0, max_value=5.0, value=3.0, step=0.1)
    
#     # Button to add movie
#     if st.button("Add Movie"):
#         # Call the /add_movie/ endpoint
#         response = requests.post(f"{API_URL}/add_movie/", params={"movie_title": new_movie, 'category': new_category,
#                                                                   'release_date': new_release_dt, 'user_rating': new_rating})
#         if response.status_code == 200:
#             st.success("Movie added successfully.")
#         else:    
#             st.error("Failed to add movie. Please try again.")

# import streamlit as st
# import requests
# from myapp import recommender

# # Base URL for your FastAPI server (using Docker Compose networking)
# API_URL = "http://backend:8000"

# st.title("Movie Recommender")

# # Input for movie selection
# movies_list = recommender.get_movies_list()
# movie_input = st.selectbox(
#     label="Select a Movie",
#     options=movies_list,
#     help="Select a movie to get recommendations"
# )

# if movie_input:
#     movie_input = movie_input.lower()

# # Helper function to handle recommendation clicks
# def handle_click(movie_id, title):
#     response = requests.post(f"{API_URL}/click/", params={"movie_id": movie_id})
#     if response.status_code == 200:
#         st.success(f"Registered click for {title}")
#     else:
#         st.error("Error registering click.")

# # Main recommendations section
# if st.button("Get Recommendations"):
#     if movie_input:
#         with st.spinner("Fetching recommendations..."):
#             response = requests.get(f"{API_URL}/recommend/", params={"movie": movie_input})
#         if response.status_code == 200:
#             data = response.json()
#             recs = data.get("recommendations", [])
#             if recs:
#                 st.subheader("Recommendations:")
#                 # Limit to 4 recommendations and create dynamic columns
#                 num_recs = min(len(recs), 4)
#                 cols = st.columns(num_recs)
#                 for idx, rec in enumerate(recs[:num_recs]):
#                     with cols[idx]:
#                         title = rec["title"].capitalize()
#                         movie_id = rec["movie_id"]
#                         st.write(f"**{title}**")
#                         if st.button(f"Select {title}", key=f"click_{movie_id}"):
#                             handle_click(movie_id, title)
#                         # Display click statistics using a metric widget
#                         stats_response = requests.get(f"{API_URL}/click_stats/", params={"movie_id": movie_id})
#                         if stats_response.status_code == 200:
#                             stats = stats_response.json()
#                             click_percentage = stats.get("click_percentage", 0)
#                             st.metric(label="Click Rate", value=f"{click_percentage:.1f}%")
#             else:
#                 st.info("No recommendations found.")
#         else:
#             st.error("Failed to fetch recommendations. Please try again.")
#     else:
#         st.warning("Please select a movie.")

# # Sidebar for adding a new movie
# with st.sidebar:
#     st.header("Add a New Movie")
#     with st.form(key="add_movie_form"):
#         new_movie = st.text_input("Movie Name")
#         new_category = st.selectbox(
#             label="Movie Category",
#             options=[
#                 "Action", "Adventure", "Animation", "Children", "Comedy", "Crime",
#                 "Documentary", "Drama", "Fantasy", "Film-Noir", "Horror", "Musical",
#                 "Mystery", "Romance", "Sci-Fi", "Thriller", "War", "Western"
#             ]
#         )
#         new_release_dt = st.date_input("Release Date")
#         new_rating = st.slider("Rating", min_value=1.0, max_value=5.0, value=3.0, step=0.1)
#         submit = st.form_submit_button("Add Movie")
#     if submit:
#         # Format the date as required by your backend (e.g., DD-Mmm-YYYY)
#         release_date_str = new_release_dt.strftime("%d-%b-%Y")
#         response = requests.post(
#             f"{API_URL}/add_movie/",
#             params={
#                 "movie_title": new_movie.lower(),
#                 "category": new_category.lower(),
#                 "release_date": release_date_str,
#                 "user_rating": new_rating
#             }
#         )
#         if response.status_code == 200:
#             st.success("Movie added successfully.")
#         else:
#             st.error("Failed to add movie. Please try again.")

# import streamlit as st
# import requests
# from myapp import recommender

# # Base URL for your FastAPI server (using Docker Compose networking)
# API_URL = "http://backend:8000"

# st.title("Movie Recommender")

# # Input for movie selection
# movies_list = recommender.get_movies_list()
# movie_input = st.selectbox(
#     label="Select a Movie",
#     options=movies_list,
#     help="Select a movie to get recommendations"
# )

# if movie_input:
#     movie_input = movie_input.lower()

# # Helper function to handle recommendation clicks
# def handle_click(movie_id, title):
#     response = requests.post(f"{API_URL}/click/", params={"movie_id": movie_id})
#     if response.status_code == 200:
#         st.success(f"Registered click for {title}")
#     else:
#         st.error("Error registering click.")

# # Main recommendations section
# if st.button("Get Recommendations"):
#     if movie_input:
#         with st.spinner("Fetching recommendations..."):
#             response = requests.get(f"{API_URL}/recommend/", params={"movie": movie_input})
#         if response.status_code == 200:
#             data = response.json()
#             recs = data.get("recommendations", [])
#             if recs:
#                 st.subheader("Recommendations:")
#                 # Create a table header using columns
#                 header_col1, header_col2, header_col3 = st.columns([3, 2, 2])
#                 header_col1.markdown("**Title**")
#                 header_col2.markdown("**Action**")
#                 header_col3.markdown("**Click Rate**")
                
#                 # Loop through each recommendation to create a row in the table
#                 for rec in recs:
#                     title = rec["title"].capitalize()
#                     movie_id = rec["movie_id"]
                    
#                     row_col1, row_col2, row_col3 = st.columns([3, 2, 2])
#                     row_col1.write(title)
                    
#                     # Button for registering a click
#                     if row_col2.button("Select", key=f"click_{movie_id}"):
#                         handle_click(movie_id, title)
                    
#                     # Fetch and display the click percentage
#                     stats_response = requests.get(f"{API_URL}/click_stats/", params={"movie_id": movie_id})
#                     click_percentage = 0.0
#                     if stats_response.status_code == 200:
#                         stats = stats_response.json()
#                         click_percentage = stats.get("click_percentage", 0)
#                     row_col3.metric(label="", value=f"{click_percentage:.1f}%")
#             else:
#                 st.info("No recommendations found.")
#         else:
#             st.error("Failed to fetch recommendations. Please try again.")
#     else:
#         st.warning("Please select a movie.")

# # Sidebar for adding a new movie
# with st.sidebar:
#     st.header("Add a New Movie")
#     with st.form(key="add_movie_form"):
#         new_movie = st.text_input("Movie Name")
#         new_category = st.selectbox(
#             label="Movie Category",
#             options=[
#                 "Action", "Adventure", "Animation", "Children", "Comedy", "Crime",
#                 "Documentary", "Drama", "Fantasy", "Film-Noir", "Horror", "Musical",
#                 "Mystery", "Romance", "Sci-Fi", "Thriller", "War", "Western"
#             ]
#         )
#         new_release_dt = st.date_input("Release Date")
#         new_rating = st.slider("Rating", min_value=1.0, max_value=5.0, value=3.0, step=0.1)
#         submit = st.form_submit_button("Add Movie")
#     if submit:
#         # Format the date as required by your backend (e.g., DD-Mmm-YYYY)
#         release_date_str = new_release_dt.strftime("%d-%b-%Y")
#         response = requests.post(
#             f"{API_URL}/add_movie/",
#             params={
#                 "movie_title": new_movie.lower(),
#                 "category": new_category.lower(),
#                 "release_date": release_date_str,
#                 "user_rating": new_rating
#             }
#         )
#         if response.status_code == 200:
#             st.success("Movie added successfully.")
#         else:
#             st.error("Failed to add movie. Please try again.")

import streamlit as st
import requests
from myapp import recommender

# Base URL for your FastAPI server (using Docker Compose networking)
API_URL = "http://backend:8000"

st.title("Movie Recommender")

# Input for movie selection
movies_list = recommender.get_movies_list()
movie_input = st.selectbox(
    label="Select a Movie",
    options=movies_list,
    help="Select a movie to get recommendations"
)

if movie_input:
    movie_input = movie_input.lower()

# Helper function to handle thumbs up (using the existing click endpoint)
def handle_thumbsup(movie_id, title):
    response = requests.post(f"{API_URL}/click/", params={"movie_id": movie_id})
    if response.status_code == 200:
        st.success(f"Registered thumbs up for {title}")
    else:
        st.error("Error registering thumbs up.")

# Main recommendations section
if st.button("Get Recommendations"):
    if movie_input:
        with st.spinner("Fetching recommendations..."):
            response = requests.get(f"{API_URL}/recommend/", params={"movie": movie_input})
        if response.status_code == 200:
            data = response.json()
            recs = data.get("recommendations", [])
            if recs:
                st.subheader("Recommendations:")
                # Create a table header using columns
                header_col1, header_col2, header_col3 = st.columns([3, 2, 2])
                header_col1.markdown("**Title**")
                header_col2.markdown("**Action**")
                header_col3.markdown("**👍 Rate**")
                
                # Loop through each recommendation to create a row in the table
                for rec in recs:
                    title = rec["title"].capitalize()
                    movie_id = rec["movie_id"]
                    
                    row_col1, row_col2, row_col3 = st.columns([3, 2, 2])
                    row_col1.write(title)
                    
                    # Button for thumbs up with an emoji
                    if row_col2.button("👍", key=f"thumbs_up_{movie_id}"):
                        handle_thumbsup(movie_id, title)
                    
                    # Fetch and display the thumbs up percentage (from the click_stats endpoint)
                    stats_response = requests.get(f"{API_URL}/click_stats/", params={"movie_id": movie_id})
                    thumbs_percentage = 0.0
                    if stats_response.status_code == 200:
                        stats = stats_response.json()
                        thumbs_percentage = stats.get("click_percentage", 0)
                    row_col3.metric(label="", value=f"{thumbs_percentage:.1f}%")
            else:
                st.info("No recommendations found.")
        else:
            st.error("Failed to fetch recommendations. Please try again.")
    else:
        st.warning("Please select a movie.")

# Sidebar for adding a new movie
with st.sidebar:
    st.header("Add a New Movie")
    with st.form(key="add_movie_form"):
        new_movie = st.text_input("Movie Name")
        new_category = st.selectbox(
            label="Movie Category",
            options=[
                "Action", "Adventure", "Animation", "Children", "Comedy", "Crime",
                "Documentary", "Drama", "Fantasy", "Film-Noir", "Horror", "Musical",
                "Mystery", "Romance", "Sci-Fi", "Thriller", "War", "Western"
            ]
        )
        new_release_dt = st.date_input("Release Date")
        new_rating = st.slider("Rating", min_value=1.0, max_value=5.0, value=3.0, step=0.1)
        submit = st.form_submit_button("Add Movie")
    if submit:
        # Format the date as required by your backend (e.g., DD-Mmm-YYYY)
        release_date_str = new_release_dt.strftime("%d-%b-%Y")
        response = requests.post(
            f"{API_URL}/add_movie/",
            params={
                "movie_title": new_movie.lower(),
                "category": new_category.lower(),
                "release_date": release_date_str,
                "user_rating": new_rating
            }
        )
        if response.status_code == 200:
            st.success("Movie added successfully.")
        else:
            st.error("Failed to add movie. Please try again.")

