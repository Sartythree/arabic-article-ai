def make_seo_prompt(article):
    return f'''
🎯 **Objective**:
Transform the following Arabic article into a highly readable, SEO-optimized, and engaging piece.

📝 **Tone & Format Requirements**:
- Language: Arabic (Fusha, journalistic but clear and simple)
- Structure:
  - SEO-friendly title
  - Intro paragraph with search-intent trigger
  - Use H2 and H3 headings
  - Numbered or bulleted lists if needed
  - Embedded YouTube links as clickable calls to action
  - Conclusion with a question to encourage engagement
- Add a keywords section at the end

🧠 **Content Strategy**:
- Highlight main names, trends, or moments
- Add subheadings for each main story or artist to improve SEO
- Make each section scannable and informative
- Use bold statements, data points, or time markers to increase authority

🔍 **SEO Optimization Instructions**:
- Add relevant keywords naturally in titles and throughout the article
- Use strong opening hook to match trending search intent
- Optimize for voice search and snippets by using questions or listicles

🛠 **DO NOT**: Do not translate, summarize, or remove core content.

📄 **Source Article**:
{article}
'''
