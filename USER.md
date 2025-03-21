# User guide

- [User guide](#user-guide)
  - [Grading](#grading)
    - [Students](#students)
    - [Create assignment](#create-assignment)
    - [Fetch assignment](#fetch-assignment)
  - [Logging into server](#logging-into-server)
  - [Save notebooks to GitHub](#save-notebooks-to-github)
    - [1. Create GitHub account](#1-create-github-account)
    - [2. Create GitHub repository](#2-create-github-repository)
    - [3. Setup GitHub authentication on server](#3-setup-github-authentication-on-server)
    - [4. Clone repository](#4-clone-repository)
    - [5. Add \& commit \& push notebooks on server to GitHub](#5-add--commit--push-notebooks-on-server-to-github)
    - [6. Pull changes from GitHub to server](#6-pull-changes-from-github-to-server)
  - [Install own software](#install-own-software)
  - [Jupyter server logs](#jupyter-server-logs)

## Grading

One user is the grader on the machine following section is for that user.

### Students

Assigning students to courses can be managed with [nbgrader labextension & cli](https://nbgrader.readthedocs.io/en/stable/user_guide/managing_the_database.html#managing-students).

The student id is a posix username in the VM.
In a ewatercycle VM, users can be added during workspace creation or with [Surf Research Access Management](https://sram.surf.nl/) or later with `sudo adduser`.
After sram invite a cronjob will add the user to the VM. Login with totp as password.
Users added to sram need to be added to nbgrader manually.

### Create assignment

1. In menu goto Nbgrader -> Formgrader -> Manage Assignments -> Add new Assignment.
2. Click on edit to navigate to folder (`~/course1/source/<name of assignment>`).
3. Create a notebook with assignment annotations using the `Create Assignment` sidebar.
4. In FormGrader press Generate, Preview, Release buttons.

### Fetch assignment

1. In menu got Nbgrader -> Assignments
2. Press fetch button

## Logging into server

You should have recieved a invitation to a eWatercycle collaborative organization, please follow instructions in email.

The username you should use to login can be found on on [SRC dashboard profile page](https://portal.live.surfresearchcloud.nl/profile)

1. To login to the Explorer or Jupyter environment, you should setup TOTP on [SRC dashboard profile page](https://portal.live.surfresearchcloud.nl/profile), this is your password on the server.
2. Optionally to login into machine with `ssh`, your SSH public key on your laptop/workstation must be added to [https://sbs.sram.surf.nl/profile](https://sbs.sram.surf.nl/profile)

## Save notebooks to GitHub

The Jupyter notebooks that you write should be saved outside the Jupyter server.
Code like notebooks can be saved git repositories on [GitHub](https://github.com/).


### 1. Create GitHub account

To store notebooks in a repository on GitHub you need an account.
Goto [https://github.com/signup](https://github.com/signup) to create an account.

### 2. Create GitHub repository

1. Goto [https://github.com/new](https://github.com/new) to create a repository.
2. Fill the form

    - For .gitignore select the `Python` template, it will prevent you from commiting auto generated files
    - Make sure to pick a license like Apache-2.0 so others know what they can do with code in the repository

### 3. Setup GitHub authentication on server

To clone private repositories or push changes to public repositories you need to setup authentication against GitHub.
You can do this by creating a [SSH key pair](https://en.wikipedia.org/wiki/Public-key_cryptography) on the server and [register the public key on GitHub](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account).

1. On the server open a terminal.
2. Create a SSH key pair with following command

    ```shell
    ssh-keygen -t ed25519 -C "your_email@example.com" -N "" -f ~/.ssh/id_ed25519
    ```

    Replace `your_email@example.com` with the email adress you used for your GitHub account.

3. Copy the content of `~/.ssh/id_ed25519.pub` to clipboard.

    In a Jupyter terminal run `cat ~/.ssh/id_ed25519.pub`, select the content, use SHIFT-right click to get context menu and then select `copy`)
4. Register the public key on GitHub by going to [https://github.com/settings/ssh/new](https://github.com/settings/ssh/new)

    1. For title use name of server where you generated SSH key pair.
    2. Paste contents of clipboard in key text area.
    3. Press green button to add the key

You are now ready to clone a repository.

> For brevity and easyness only SSH key pair without passphrase is explained, see [GitHub docs](https://docs.github.com/en/get-started/getting-started-with-git/about-remote-repositories) for alternatives and more secure methods.

### 4. Clone repository

On the GitHub repository page there is a green `Code` button, open it to get the SSH git URL of the repository.
It should look something like `git@github.com:<user name>/<repository>.git`

1. On the server open a terminal
2. Run the following command to clone a repo

    ```shell
    git clone git@github.com:<user name>/<repository>.git
    ```

    Replace `<user name>` and `<repository>` with your username and repository name respectivly.

      - For the first time it will prompt if you want to connect to github.com, enter `yes` followed by enter.

You will now have a local copy of the repository.

### 5. Add & commit & push notebooks on server to GitHub

Following commands should be run in a terminal on the server inside the repository directory.

To add a file to git staging use

```shell
git add <filename>
```

To commit the file to git you first need tell git who you are with

```shell
git config --global user.email "your_email@example.com"
git config --global user.name "Your Name"
```

(Replace `your_email@example.com` with the email adress you used for your GitHub account and fill in your full name)

To commit use

```shell
git commit -m "some message"
```

Replace `some message` text that describes changes that where made since last commit.

Now your changes have been saved locally, to push them to GitHub use

```shell
git push
```

### 6. Pull changes from GitHub to server

If files on GitHub and you want to pull those changes to the server then in terimal use

```shell
git pull
```

> The git commands can also be done using the [Git tab](https://github.com/jupyterlab/jupyterlab-git) in the Jupyter Lab environment.

## Install own software

The default Jupyter kernel is read-only and has the eWaterCycle Python package and friends installed.
To install additional Python or Conda packages you need to create your own conda environment with a Jupyter kernel.

1. Install eWaterCycle Python package dependencies with user chosen Conda environment name.

- Get the eWaterCycle `environment.yml` file:

```shell
wget https://raw.githubusercontent.com/eWaterCycle/ewatercycle/main/environment.yml
```

- Create your own conda environment e.g. `testewatercycle`:

```shell
mamba env create --file environment.yml --name testewatercycle
```

2. Install eWaterCycle Python package

- Activate your own conda environment e.g. `testewatercycle`:

```shell
conda activate testewatercycle
```

- Install eWaterCycle Python package:

```shell
pip install ewatercycle
```

or 

```shell
pip install -e .[dev]
```

to be in development mode if you have the source code.

3. Install Jupyter kernel

- Install `ipykernel`:

```shell
mamba install -c conda-forge ipykernel
```

- Get the path to python in our own conda environment:

```shell
which python
```

> that returns `/home/usr/.conda/envs/testewatercycle/bin/python`

- Add it to Jupyter: 

```shell
/home/usr/.conda/envs/testewatercycle/bin/python -m ipykernel install --user --name 'testewatercycle'
```

> that returns `Installed kernelspec testewatercycle in /home/usr/.local/share/jupyter/kernels/testewatercycle`

4. Restart your own Jupyter server from tab `File > Hub Control Panel`

5. Open a notebook and pick the new kernel that is `testewatercycle`

6. Install additional software

## Jupyter server logs

Sometimes something goes wrong in the Jupyter Server, for example you expected to see an error in your notebook but it is not there.

The log of the Jupyter server can be viewed with

```shell
journalctl -f -u jupyter-vagrant-singleuser.service
```

Replace `vagrant` with own username.
