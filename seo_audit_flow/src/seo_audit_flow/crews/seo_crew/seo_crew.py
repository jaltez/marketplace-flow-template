import os
from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import ScrapeWebsiteTool

@CrewBase
class SeoCrew():
	"""SEO Audit Crew for analyzing a single webpage"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	def __init__(self):
		"""Initialize with the URL to analyze"""

		self.scrape_tool = ScrapeWebsiteTool()

	@agent
	def content_fetcher(self) -> Agent:
		return Agent(
			config=self.agents_config['content_fetcher'],
			tools=[self.scrape_tool],
			verbose=True
		)

	@agent
	def on_page_analyzer(self) -> Agent:
		return Agent(
			config=self.agents_config['on_page_analyzer'],
			verbose=True
		)

	@agent
	def report_generator(self) -> Agent:
		return Agent(
			config=self.agents_config['report_generator'],
			verbose=True
		)

	@task
	def fetch_content_task(self) -> Task:
		return Task(
			config=self.tasks_config['fetch_content_task'],
		)

	@task
	def analyze_page_task(self) -> Task:
		return Task(
			config=self.tasks_config['analyze_page_task'],
		)

	@task
	def generate_report_task(self) -> Task:
		return Task(
			config=self.tasks_config['generate_report_task'],
			output_file='seo_audit_report.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the SEO Audit crew"""

		llm = LLM(
			model=os.getenv("MODEL"),
			base_url=os.getenv("API_BASE")
		)

		return Crew(
			agents=self.agents,
			tasks=self.tasks,
			process=Process.sequential,
			llm=llm,
			verbose=True,
		)
