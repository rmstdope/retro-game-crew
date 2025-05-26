
from typing import List
from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class GameBuilderCrew:
    """GameBuilder crew"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'
    
    researching_llm = LLM(
        model='gemini/gemini-2.5-flash-preview-04-17',
        temperature=0.6,
        # max_tokens=2000,
        top_p=1,
    )
    hacking_llm = LLM(
        model='gemini/gemini-2.5-flash-preview-04-17',
        temperature=1.0,
        max_tokens=20000,
        top_p=1,
    )
    qa_llm = LLM(
        model='gemini/gemini-2.5-flash-preview-04-17',
        temperature=0.1,
        max_tokens=20000,
        top_p=0.5,
    )

    @agent
    def game_researcher_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['game_researcher'],
            llm=self.researching_llm,
            allow_delegation=False,
            # reasoning=True,
            verbose=True
        )
    
    def hardcore_hacker_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['hardcore_hacker'],
            llm=self.hacking_llm,
            allow_delegation=False,
            # reasoning=True,
            verbose=True
        )
    
    @agent
    def validation_engineer_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['validation_engineer'],
            llm=self.qa_llm,
            allow_delegation=False,
            # reasoning=True,
            verbose=True
        )
    
    @agent
    def verification_engineer_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['verification_engineer'],
            llm=self.qa_llm,
            allow_delegation=True,
            # reasoning=True,
            verbose=True
        )
    

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['game_research'],
            agent=self.game_researcher_agent(),
        )

    @task
    def code_task(self) -> Task:
        return Task(
            config=self.tasks_config['coding'],
            agent=self.hardcore_hacker_agent(),
        )

    @task
    def validation_task(self) -> Task:
        return Task(
            config=self.tasks_config['validate'],
            agent=self.validation_engineer_agent(),
        )

    @task
    def verification_task(self) -> Task:
        return Task(
            config=self.tasks_config['verify'],
            agent=self.verification_engineer_agent(),
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True, 
        )
