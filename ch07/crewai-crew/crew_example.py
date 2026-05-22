"""
(C) Copyright 2026 Boni Garcia (https://bonigarcia.github.io/)
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
 http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
from crewai import Agent, Task, Crew, Process


def main():
    # 1. Define Agents with specialized roles and goals
    # Each agent has its own local context (instructions and role)
    researcher = Agent(
        role='Tech Researcher',
        goal='Analyze the latest trends in {topic}',
        backstory='You are an expert researcher at a major tech publication.',
        verbose=True
    )

    writer = Agent(
        role='Content Writer',
        goal='Write a blog post about {topic} based on the research',
        backstory='You are a skilled writer who specializes in making complex tech topics accessible.',
        verbose=True
    )

    editor = Agent(
        role='Senior Editor',
        goal='Review the blog post for clarity, tone, and technical accuracy',
        backstory='You are a meticulous editor with an eye for detail and a passion for quality.',
        verbose=True
    )

    # 2. Define Tasks
    # Tasks define the flow of context from one agent to the next
    research_task = Task(
        description='Identify the 3 most significant trends in {topic} for 2026.',
        expected_output='A detailed report on the top 3 trends.',
        agent=researcher
    )

    writing_task = Task(
        description='Write a 500-word blog post about {topic} using the research provided.',
        expected_output='A well-structured blog post in Markdown format.',
        agent=writer,
        context=[research_task]  # Explicitly passing context from the research task
    )

    editing_task = Task(
        description='Review and polish the blog post about {topic}.',
        expected_output='A final, polished version of the blog post.',
        agent=editor,
        context=[writing_task]  # Explicitly passing context from the writing task
    )

    # 3. Form the Crew and define the process
    # The 'Sequential' process ensures that context flows logically from research -> writing -> editing
    crew = Crew(
        agents=[researcher, writer, editor],
        tasks=[research_task, writing_task, editing_task],
        process=Process.sequential,
        verbose=True
    )

    # 4. Execute the crew's work
    print("Starting CrewAI collaboration...")
    result = crew.kickoff(inputs={'topic': 'Context Engineering'})

    print("\nFinal Result:")
    print(result)


if __name__ == "__main__":
    main()
