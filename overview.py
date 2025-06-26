import streamlit as st

# Page Title
st.title("AI and Collusion")

# Placeholder for Markdown content
article_content = """

The rise of AI is linked to the phenomenon of algorithmic collusion. We may wonder:

- Do algorithms make collusion easier?
- Should we ban pricing algorithms?  
- What can be done to check, fix, etc.?

Short answers: yes, yes, a lot.

Now with a bit more detail:

### Do algorithms make collusion easier? 

Yes, they do in so far as automation makes anything easier to implement, algorithms also make collusion easier. But making collusion easier with algorithms requires collusion between algorithm designers. This is the main point we make in our latest work.

Algorithms can automate collusion for us. 

### Does this mean we should ban all algorithms?

No. Companies can establish price collusion, but we do not ban companies. Because, just as we can use algorithms to automate collusion, we can also use them to automate competition.

### What can be done to regulate algorithmic collusion?

We must allow for algorithms that are *designed competitively*, and lead to competitive pricing. On the other hand, we must identify algorithms that are **orchestrated**, and lead to collusive pricing. 

### Our proposal

We distinguish competitively designed algorithms from orchestrated algorithms by treating the algorithms as strategies, and determining whether or not the picked algorithm is a selfish profit maximising best response to the market.
"""

# Display image
st.image("images/age_of_ai.png", caption="Algorithms change competition and collusion.")

# Display Markdown content
st.markdown(article_content)
