
from typing import List
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class GameBuilderCrew:
    """GameBuilder crew"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def game_researcher_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['game_researcher'],
            allow_delegation=False,
            verbose=True
        )
    
    def hardcore_hacker_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['hardcore_hacker'],
            allow_delegation=False,
            verbose=True
        )
    
    @agent
    def validation_engineer_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['validation_engineer'],
            allow_delegation=False,
            verbose=True
        )
    
    @agent
    def verification_engineer_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['verification_engineer'],
            allow_delegation=True,
            verbose=True
        )
    

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['game_research'],
            agent=self.game_researcher_agent(),
            output_file='output/research.txt'
        )

    @task
    def code_task(self) -> Task:
        return Task(
            config=self.tasks_config['coding'],
            agent=self.hardcore_hacker_agent(),
            output_file='output/game.py'
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
