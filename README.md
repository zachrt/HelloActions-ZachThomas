# HelloActions-ZachThomas

## Workflow Explanation
* **What is the purpose of the on section?** It defines the events that trigger the workflow, such as a push to the main branch.
* **What does workflow_dispatch do?** It allows the workflow to be executed manually from the GitHub Actions tab.
* **What does runs-on specify?** It specifies the operating system environment (like ubuntu-latest) where the job will run.
* **Why is actions/checkout needed?** It pulls the repository's code into the runner environment so the workflow can access your files.
* **What does the language setup action do?** It installs and configures the specific programming language environment on the runner (though our Python script uses the system default in this specific example).
* **What is the difference between compiling and running the program?** Compiling translates source code into machine code, while running executes it.
* **Where can you see the program output?** In the GitHub Actions tab, within the log details of the workflow run's execution step.
* **What is the difference between a workflow, a job, and a step?** A workflow is the automated process, a job is a set of steps on a single runner, and a step is a single task or command.

**AI Usage Statement:** AI (Gemini) was used to generate the boilerplate code and terminal commands for this lab assignment.
