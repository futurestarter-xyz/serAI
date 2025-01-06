from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class Icosfyi():
    """Icosfyi crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def marketing_strategist(self) -> Agent:
        return Agent(
            config=self.agents_config['marketing_strategist'],
            verbose=True
        )

    @agent
    def crypto_community_architect(self) -> Agent:
        return Agent(
            config=self.agents_config['crypto_community_architect'],
            verbose=True
        )

    @agent
    def growth_hacking_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['growth_hacking_analyst'],
            verbose=True
        )

    @agent
    def content_and_seo_strategist(self) -> Agent:
        return Agent(
            config=self.agents_config['content_and_seo_strategist'],
            verbose=True
        )

    @agent
    def technical_integration_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['technical_integration_specialist'],
            verbose=True
        )

    @task
    def marketing_strategy_research(self) -> Task:
        return Task(
            config=self.tasks_config['marketing_strategy_research'],
        )

    @task
    def community_engagement_blueprint(self) -> Task:
        return Task(
            config=self.tasks_config['community_engagement_blueprint'],
        )

    @task
    def growth_hacking_and_acquisition_plan(self) -> Task:
        return Task(
            config=self.tasks_config['growth_hacking_and_acquisition_plan'],
        )

    @task
    def content_and_visibility_strategy(self) -> Task:
        return Task(
            config=self.tasks_config['content_and_visibility_strategy'],
        )

    @task
    def technical_platform_optimization(self) -> Task:
        return Task(
            config=self.tasks_config['technical_platform_optimization'],
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )