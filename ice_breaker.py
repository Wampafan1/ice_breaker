
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from third_parties.linkedin import scrape_linkindin_profile


if __name__ == "__main__":
    load_dotenv()

    summary_template = """
         given the information {information} about a person from I want you to create:
         1. a short summary
         2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_values="information", template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    
    chain = summary_prompt_template | llm
    
    linkedin_data = scrape_linkindin_profile(linkedin_profile_url="https://www.linkedin.com/in/the-real-joe/", mock=True)

    res = chain.invoke(input={"information": linkedin_data})

    print(res)

