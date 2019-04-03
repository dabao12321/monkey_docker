
def spawn_dockerfile(dir, python_ver=3, expose_port=80):
    '''
    Sets path

    dir: string path of directory
    python_ver: 3 or 2.7
    expose_port: make this port availible to world outside container
    '''
    with open("Dockerfile", "w") as f:
        f.write("FROM python:"+ str(python_ver) +"\n")
        f.write("WORKDIR /"+ dir+"\n")
        f.write("COPY . /"+ dir+"\n")
        # assuming directory contains requirements.txt
        f.write("RUN pip install --trusted-host pypi.python.org -r requirements.txt"+"\n")
        f.write("CMD [\"python\"]"+"\n")

if __name__ == "__main__":
    spawn_dockerfile("testing")
