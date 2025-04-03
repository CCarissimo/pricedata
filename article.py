import streamlit as st

# Page Title
st.title("Algorithmic Collusion by Algorithm Orchestration")

# Placeholder for Markdown content
article_content = """
Do algorithms make collusion easier? In short, yes.
In so far as automation makes things easier, algorithms also make collusion easier.
But making collusion easier with algorithms requires collusion between algorithm designers.
This is the main point we make in our latest work.

Algorithms can automate collusion for us. Does this mean we should ban all algorithms?
No. Companies can establish price collusion, but we do not ban companies.
Because, just as we can use algorithms to automate collusion, we can also use them to automate competition.

We must allow for algorithms that are *designed competitively*, and lead to competitive pricing. On the other hand, we must identify algorithms that are **orchestrated**, and lead to collusive pricing. 

We distinguish competitively designed algorithms from orchestrated algorithms by treating the algorithms as strategies, and determining whether or not the picked algorithm is a selfish profit maximising best response to the market.

"""

# Display Markdown content
st.markdown(article_content)
