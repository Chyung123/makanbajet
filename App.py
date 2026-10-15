import streamlit as st 
import pandas as pd

#Set up the website
st.set_page_config(
  page_title="MakanBajet",
  page_icon="🍚"
)

st.title("🍚 MakanBajet")
st.write("Find affordable meals near your campus!")

st.info("Demo only:All food is fictional.")

#Sample food data
foods = [
  {"food": "Roti Canai", "vendor": "Canteen A",
   "price": 2.50, "category": "Others"},

  {"food": "Nasi Lemak", "vendor": "Canteen B",
   "price": 5.50, "category": "Rice"},
  
  {"food": "Maggi Goreng", "vendor": "Canteen C",
   "price": 3.50, "category": "Noodles"},

  {"food": "Chicken Rice", "vendor": "Canteen D",
   "price": 6.50, "category": "Rice"},

  {"food": "Curry Mee", "vendor": "Canteen E",
   "price": 4.50, "category": "Noodles"},

  {"food": "Fried Rice", "vendor": "Canteen F",
   "price": 5.50, "category": "Rice"}

]

df = pd.DataFrame(foods)

#User chooses budget
budget = st.slider(
  "Your maximum budget(RM)",
  min_value = 3,
  max_value = 20,
  value = 8
)

#User chooses food category
category = st.selectbox(
  "Food Category",
  ["All“,"Rice","Noodles","Rice","Others"]
)

#User searches for food
search = st.text_input(
     "Search food",
     placeholder= "e.g. Chicken Rice"
)

#Filter by budget
results = df[df["price"] <= budget]

#Filter by category
if category != "All":
   results = results[
        results["category"] == category 
   ]

#Filter by food name
if search:
   results = results[
      results["food"].str.contains(
          search,
          case = False,
          regex = False
      )
    ]

#Show cheapest food first
results = results.sort_values("price")

st.subheader("Available Meals")
st.write(f"Found {len(results)} meals")

if results.empty:
   st.warning("No food found. Try another budget.")

else:
   for _,meal in results.iterrows():
       with st.container(border=True):
           st.subheader(
              f"{meal['food']} - RM{meal['price']:2f}"
              )
              st.write(meal["vendor"])

st.caption(meal["category"])

st.divider()
st.caption("MakanBajet VO.1 | Student Project")
          

  
  
  
     
