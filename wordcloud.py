import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

text = ''''
About the job
Artisan is seeking an AI Engineer to become part of our rapidly expanding team. We're creating the most advanced AI employees on the market and exceptional software products for them and human teams to use, starting with sales and rapidly expanding into other verticals. We were a part of the Y Combinator W24 batch, have raised over $7.4M in seed capital, and are relentlessly working to become the market leader in this space and build the future of work and software.
If you pursue excellence in your work, thrive in fast-paced settings and are an extraordinarily talented backend engineer with a strong educational and career background, we would love to hear from you!

Key Responsibilities:
Fine-tuning and prompt engineering LLMs for our Artisans, helping us to create the most advanced AI Employees (primarily Google's Gemini, OpenAI's GPT 3.5, GPT 4 & GPT-4o, and Anthropic's Claude).
Developing systems to allow users to interact with platform features through chat (e.g. our onboarding flow and platform setup is currently done by Ava, The Sales Rep Artisan).
Architect LLM systems which integrate with third-party tools for a plethora of Artisan use cases (think email conversations, the user chat interface, etc.)
Minimize occurrences of hallucinations and strange tone of voice.
Develop new email Playbooks which execute research & writing workflows typically done by human sales reps.
Reduce latency of our LLM systems.
Stay up-to-date with the latest LLM technologies so we stay on the bleeding edge of what's possible.

Qualifications:
Degree in Computer Science, Machine Learning, Data Science, or a related field.
Industry experience with LLM fine tuning and prompt engineering.
Excellent written and spoken English.
Extensive experience in Python and MLOps tools like MLFlow and cloud platforms such as Azure or AWS.
Expertise in Python back-end development.
'''


# generate word cloud for the given `text` variable
# please use existing libraries to generate word cloud and save it as PNG

wordcloud = WordCloud(background_color="white", max_words=2000, width=1000, height=600).generate(text)