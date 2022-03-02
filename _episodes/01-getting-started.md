---
title: "Getting Started"
teaching: 15
exercises: 0
questions:
- "How do I use Spyder?"
- "How can I run Python programs?"
- "<b>Armin</b>"
objectives:
- "Learners can launch Spyder"
- "Learners are able to use the IPython console to interact with Python"
- "Learners are able to write code in the Spyder editor and run this code"
- "Learners are able to save their code in a *.py file"
- "Learners can use the different buttons and panels needed in Spyder"
keypoints:
- "Use Spyder for editing and running Python"
- "The IPython console can be used to interact with Python directly"
- "The editor can be used to write code, run and save it"
---

## Use Spyder for editing and running Python.

*   The [Anaconda package manager][anaconda] is an automated way to install the [Spyder IDE][spyder] (Integrated Development Environment).
    *   See [the setup instructions]({{ page.root }}/setup.html) for Anaconda installation instructions.
*   It also installs all the extra libraries it needs to run.
*   Once you have installed Python and the Spyder, you can run it via a click on the icon under Apps or open a shell and type:
    ~~~
    $ spyder
    ~~~
    {: .python}

*   This will start the Spyder IDE.
*   This environment has several useful tools we can use, which you can see in different panels in Spyder. We will look into some of them.
* You can change the positions and sizes of these panels to your preference, as you get to know them.

## Different ways of interacting with Python using Spyder

*   On the left, filling half of the screen is the editor. Here you can write and edit code, which can then be saved in a file (usually with a .py extension). We can run the code we wrote here by pressing the green 'play' button on top or press F5 on your keyboard.
*   On the bottom right, we find the IPython console. This is were we can talk directly to Python. It will interpret what you have typed directly when you press Enter.

## Python in the console

> Go to the IPython tab at the bottom right. What happens when you type a small calculation there?
> For example, what happens when you type the following calculation and press enter?
> ~~~
> 7 * 3
> ~~~
> {: .python}
>
> > ## Solution
> >
> > Python returns the result of the calculation.
> > ~~~
> > 21
> > ~~~
> > {: .python}
> {: .solution}
{: .challenge}

> ## Python in the editor
>
> The large panel on the left probably has some text in it that looks like this:
> ~~~
> """
> Spyder Editor
>
> This is a temporary script file.
> """
>~~~
> Write the following line below these lines and press run (use the button with both the cursor and the green 'play' button to run a single line or a selected bit of code). 
> What happens?
>
> ~~~
> print('Hello world!')
> ~~~
> {: .python}
>
> > ## Solution
> >
> > In the IPython console  Python tells you which files it ran and the result of this run
> > ~~~
> > runfile('/home/ylja/.config/spyder-py3/temp.py', wdir='/home/ylja/.config/spyder-py3')
> > Hello world!
> > ~~~
> > {: .python}
> {: .solution}
{: .challenge}

* Code written in the editor can be saved, like any other file.

> ## Saving the code
>
> To save the code, press 'file' and then 'save as'. Now give the file a name, for example 'mycode.py' and save it in a directory/folder where you know how to find it.
> Look into your file system the way you usually do it. Is the file where you expect it to be?
>
> {: .python}
{: .challenge}



[anaconda]: https://docs.anaconda.com/anaconda/install/
[spyder]: https://www.spyder-ide.org/
