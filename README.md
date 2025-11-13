# TUTORIAL

This tutorial deals with the basics of GitHub and the Python programming language. The main audience consists of researchers, especially originating from STEM. Through many examples we will illustrate both general and particular functionnalities usefull when programming or carrying out scientific related work.

## 00 Introduction to GitHub

### Purpose

In this first section we will see what is GitHub, why we use it, and how.

Git is a distributed version control (DVC) system that allows to manage a program and its versions and track the changes made by programmers. This is very convenient as it allows to revert any change, maintain various versions of a program.

GitHub (or GitLab) is a more advanced implementation of Git providing additionnal functionnalities on top of Git such as hosting on a remote server, access control, sharing, feature requests, wiki or discussion. Github is designed to host, track and share computer programs in a collaborative environment. Each program is stored in a separate repository located on a remote server. To work on the program, a local user clones the repository in order to have a copy of the program locally. Then once the modification is satisfying it must be sent back to the remote server for everyone to enjoy it. Think about the remote version as the official one.

### Workflow

The main workflow is then as follows :
create or clone the repository > change the program > commit the changes > push the changes > change the program > and so on

Everything can be done either through command line interface (CLI) or graphical interface (GitHub desktop). I recommend using the Github desktop application.

If one wants to modify the program without risking breaking it, a parallel branch can be created. The main branch will be unaffected, ensuring the changes do not break a program that is being used. Then once the new branch is satisfying (it is checked for functionnalities and bugs), you can merge it with the main branch in order to implement its features in the main branch.
The possibility to create branches should not be used recklessly (wow !). It is not a way to maintain several sustainable versions of a program. You should do releases.

### Recommendations

One commit should cover one change and have an explicit comment. This makes tracking change and reverting them a confortable experience. If you change 20 things and do one commit with an oblivious name such as 'update' then good luck with correcting your mistakes afterwards.

Each GitHub repository should contain a documentation. A `README.md` explaining the purpose of the program and its main features is the minimum you can do. What you are reading is an example of `README.md`. Because it is written in markdown, you can structure it with titles, *format* **text**, insert [hyperlinks](https://www.youtube.com/watch?v=dQw4w9WgXcQ). More importantly you can write nice $\LaTeX$ equations ($U=RI$, $\frac{1}{2}mv^2$), which is very convenient to explain scientific code ! Do it.

There are few **<span style="color:red; font-size:18px">security</span>** concerns regarding the use of repositories. Every change is visible by the users of the repository and they can be reverted. If you store sensitive data in a repository, such as a private SSH key, confidential personnal information, passwords, etc. You will not be able to delete it entirely because of the tracking feature that allows to revert any changes. You will have to delete the entire repository, especially if it is public, as any random bot will sniff everything and scam you as soon as possible.

Do not store data on repositories. Indeed, because of this tracking functionnality, the repository will keep this heavy data in the history. So anyone working with the repository, will have to download it when cloning it locally. Repositories are not USB keys, it is a place to hold a program.

Also, GitHub is not a proper backup solution. You should always keep a backup somewhere.

### GitHub Copilot AI

As a scholar, Github provides an access to its GitHub copilot AI that can be implemented in an editor such as Visual Studio Code (VSC). VSC is a nice editor that I recommend. Do not rely naively on AI : AI stupid, AI evil, AI replace you soon.

## 10 Introduction to Python

In this section we will see what is Python, how to install and use it. The course will be the opportunity to get familiar with Python itself and practice the main features of Python. This is a nice introductory course to programming language in general.

Python is a free and open-source programming language widely used in a very broad range of fields such as web development, data science, artificial intelligence, scientific computing, graphical interface, command control, and much more ! Anything is possible with Python ! Due to its simplicity and readability, its huge active community, Python is ideal to learn programming in general. Keep in mind this is not the fastest language when it commes to many High-Performance Computing (HPC), so always search for already existing codes that is optimised when you lean towards this part of applications (molecular dynamics, fluidics, optimisation ...). Otherwise, switch to a faster language such as ForTran or C.

### Installation

Python programs need an interpreter, i.e a software that reads and executes Python code. This interpreter is often provided as part of a Python distribution or environment. To run Python code on your computer, you first need to install such an interpreter.

For scientific work, it’s best to use an environment manager, which helps you install, update, and isolate different versions of Python and scientific libraries. The most popular choices are Anaconda or [Miniconda](https://www.anaconda.com/download/success), which come with many scientific packages preinstalled and make environment management easier.

I advice you start with miniconda, and integrate the modules in the environment as you need them. Once installed, you can open an anaconda prompt. It is like any terminal except you have the base environment activated which allow you to run python programs. I advice you set up an environment with your desired version of Python using a command line such as

```bash
conda create -n myenv python=3.10
```

then activate the environment using

```bash
conda activate myenv
```

and install any package using `pip`

```bash
pip install numpy
```

For scientific work you should have at least `numpy`, `matplotlib` and `scipy`.

### First run of a Python program

You can execute the two following programs by typing in a terminal

```bash
python3 <name_of_program.py>
```

`10_Python_First_steps.py` is about installing python and running the first python program. Try to execute this program. You will also learn about the basics of the Python programming language.

`11_Python_Language.py` is about the Python language and tells you all the things you need to know to get started.

If you are not familiar with command line this is where I advice you install an Integrated Developping Environment. This is a text editor connected to the Python compiler. [Visual Studio Code](https://code.visualstudio.com/) is excellent ! It lets you select the python environment and run code with just a simple shortcut (`ctrl + F5`).

Then I show two other ways to execute Python program, also compatible with VSCode. They allow you to execute only parts of the program : ideal when you want to test things during the development of a program.

You can run interactve python following `12_Interactive_python.py`. This is a normal text file where the code is split into cells using `# %%`. You can then run cells independetly while the output is displayed in a separate window. This resemble `Spyder` and `Matlab` for those who know.

You can run jupyter notebooks following `13_Jupyter_notebook.ipynb`. It is very similar to interactive pythonn except here cells are explicited. Also nice during development and so on, and you can put markdown and figures nicely, so when you save the file it keeps in memory the figures and so on.

## 20 Intermediary Python

In this section we will discuss Python functionnalities oriented towards scientific concerns.

Data is an important element of the work of a scientist. From how you generate and analyse data depends the quality of their work. `21_Save_Load_file_Dice.py` deals with saving and loading data in a consistent way while `22_Plot_Dice.py` deals with plotting such data.

More advanced in the Python domain, few other programs are about using functions and classes. They are very usefull as they help structure the code and make it more efficient. See `24_Lambda_Functions.py` and `25_Class_definition.py` for more details.

Also, the way you define your variables may affect the performance of your code, and sometimes you want to save some precious seconds, minutes, or even more. `27_Perf_test.py` illustrates how simple differences can change execution time.

## 30 Python numericals

Scientists use various tools to process and interpret data. An example is the Fast Fourier Transform (FFT), [one of the most impactful algorithm](https://www.youtube.com/watch?v=nmgFG7PUHfo). But plenty of other tools have their relevance such as the Hilbert transform, Laplace transform, frequency filters, or statistical analysis. There are no needs to re write such algorithm as they are already implemented in the libraries such as `numpy` or `scipy`. This section covers the use of such algorithms for greater good.

There is also some tedious mathematical work that python can carry out for you, such as fitting the data with an analytical formula, handling errorbars or symbolic computation. Symbolic computation allows for the manipulation of analytical expression. With symbolic computation you can substitue terms, derive or integrate, handle systems of equation or solve polynomials. These symbolic computtions are harvested in order to propagate uncertainties, solve equations and carry out a Taylor expansion.

# 40 Molecular dynamics

Molecular dynamics is about determining the acceleration, velocity and position of particles in conditions where forces are known. This usually relies on initial values being interpolated to a next time step using integrations algorithms such as velocity-Verlet or Runge-Kutta. `scipy` proposes a very convenient way to carry out this procedure through its function `ivp_solve`. `42_ivp_solve_test.py` provides a nice example of its use.

# 50 Slurm cluster

Slurm is a load manager used on HPC servers. It allocates resources to tasks and handle waiting lists. This is an important feature when it comes to run its heavy computations on a remote server.

`51_job_start.sh` and `52_job_start_2.sh` are two bash programs that order to start the execution of programs on a slurm server. Contact the local administrator of the slurm server (Micheal Devereux) for more informations.

# Other things to develop

For the time being, the following elements are not developped in this tutorial, but we can discuss about it upon reasonable request :

- Multi-objective optimisation
- Graphical interface for command control

## List of contributors
* Adrien Poindron
