from generation import call

input_requirements=f"""
Consider a website where you can share book reviews. As a user of this site, you can register on the platform, add books to your profile, write and share reviews, rate books, and track your reading progress through the reading status.
"""

llm_response = call(input_requirements)

