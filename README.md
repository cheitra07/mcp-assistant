cmd

pip install uv
uv init mcpassistant
cd mcpassistant 
cursor .

..........
terminal

uv venv
.venv\Scripts\activate
.............
##1. trouble shoot issue
PS D:\demo-projects-2025\mcp> .venv\Scripts\activate
.venv\Scripts\activate : File D:\demo-projects-2025\mcp\.venv\Scripts\activate.ps1 cannot be loaded because running 
scripts is disabled on this system. For more information, see about_Execution_Policies at 
https:/go.microsoft.com/fwlink/?LinkID=135170.
At line:1 char:1
+ .venv\Scripts\activate
+ ~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : SecurityError: (:) [], PSSecurityException
    + FullyQualifiedErrorId : UnauthorizedAccess

................
cmd 

.venv\Scripts\activate.bat

.....................................
cursor terminal

uv add langchain-groq
uv add langchain-opanai
uv add mcp-use
uv add mcp-use --frozen

download nodejs and install 
cmd
node
--version

python --version
Install Jupyter Extension in Cursor

    Press Ctrl+Shift+X (or go to Extensions).

    Search for Jupyter and install the official one.

    Also install the Python extension if not already present.

3. Select Python Interpreter (Kernel)

    Open a .ipynb notebook file or create one.

    In the top right, you’ll see “Select Kernel”.

    Click it and choose your environment:

        Your virtual environment: .\.venv\Scripts\python.exe

        Or your base Python installation


cursor ide
file-prefrences--cursor settings --MCP--replace with our code

pip install python-dotenv
pip install langchain_groq
pip install mcp_use

uv run app.py

..........
###push to github

git init
git add .
git commit -m "first commit"
git remote origin add "repofile.git"
git push -u origin main
