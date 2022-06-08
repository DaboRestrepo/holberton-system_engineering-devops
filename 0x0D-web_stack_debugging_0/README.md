# 0x0D. Web stack debugging #0

<html>
<div class="panel panel-default" id="project-description">
 <div class="panel-body">
  <p>
   <img alt="" src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/265/uWLzjc8.jpg" style=""/>
  </p>
  <h2>
   Background Context
  </h2>
  <p>
   The Webstack debugging series will train you in the art of debugging. Computers and software rarely work the way we want (that’s the “fun” part of the job!).
  </p>
  <p>
   Being able to debug a webstack is essential for a Full-Stack Software Engineer, and it takes practice to be a master of it.
  </p>
  <p>
   In this debugging series, broken/bugged webstacks will be given to you, the final goal is to come up with a Bash script that once executed, will bring the webstack to a working state. But before writing this Bash script, you should figure out what is going on and fix it manually.
  </p>
  <p>
   Let’s start with a very simple example. My server must:
  </p>
  <ul>
   <li>
    have a copy of the
    <code>
     /etc/passwd
    </code>
    file in
    <code>
     /tmp
    </code>
   </li>
   <li>
    have a file named
    <code>
     /tmp/isworking
    </code>
    containing the string
    <code>
     OK
    </code>
   </li>
  </ul>
  <p>
   Let’s pretend that without these 2 elements, my web application cannot work.
  </p>
  <p>
   Let’s go through this example and fix the server.
  </p>
  <pre><code>vagrant@vagrant:~$ docker run -d -ti ubuntu:14.04
Unable to find image 'ubuntu:14.04' locally
14.04: Pulling from library/ubuntu
34667c7e4631: Already exists
d18d76a881a4: Already exists
119c7358fbfc: Already exists
2aaf13f3eff0: Already exists
Digest: sha256:58d0da8bc2f434983c6ca4713b08be00ff5586eb5cdff47bcde4b2e88fd40f88
Status: Downloaded newer image for ubuntu:14.04
76f44c0da25e1fdf6bcd4fbc49f4d7b658aba89684080ea5d6e8a0d832be9ff9
vagrant@vagrant:~$ docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
76f44c0da25e        ubuntu:14.04        "/bin/bash"         13 seconds ago      Up 12 seconds                           infallible_bhabha
vagrant@vagrant:~$ docker exec -ti 76f44c0da25e /bin/bash
root@76f44c0da25e:/# ls /tmp/
root@76f44c0da25e:/# cp /etc/passwd /tmp/
root@76f44c0da25e:/# echo OK &gt; /tmp/isworking
root@76f44c0da25e:/# ls /tmp/
isworking  passwd
root@76f44c0da25e:/#
vagrant@vagrant:~$
</code></pre>
  <p>
   Then my answer file would contain:
  </p>
  <pre><code>sylvain@ubuntu:~$ cat answerfile
#!/usr/bin/env bash
# Fix my server with these magic 2 lines
cp /etc/passwd /tmp/
echo OK &gt; /tmp/isworking
sylvain@ubuntu:~$
</code></pre>
  <p>
   Note that as you cannot use interactive software such as
   <code>
    emacs
   </code>
   or
   <code>
    vi
   </code>
   in your Bash script, everything needs to be done from the command line (including file edition).
  </p>
  <h2>
   Installing Docker
  </h2>
  <p>
   For this project you will be given a container which you can use to solve the task.
   <strong>
    If
   </strong>
   you would like to have Docker so that you can experiment with it and/or solve this problem locally, you can install it on your machine, your Ubuntu 14.04 VM, or your Ubuntu 16.04 VM if you upgraded.
  </p>
  <ul>
   <li>
    <a href="https://docs.docker.com/docker-for-mac/install/" target="_blank" title="Mac OS">
     Mac OS
    </a>
   </li>
   <li>
    <a href="https://docs.docker.com/docker-for-windows/install/" target="_blank" title="Windows">
     Windows
    </a>
   </li>
   <li>
    <a href="https://www.liquidweb.com/kb/how-to-install-docker-on-ubuntu-14-04-lts/" target="_blank" title="Ubuntu 14.04">
     Ubuntu 14.04
    </a>
    (Note that Docker for Ubuntu 14 is deprecated and you will have to make some adjustments to the instructions when installing)
   </li>
   <li>
    <a href="https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-16-04" target="_blank" title="Ubuntu 16.04">
     Ubuntu 16.04
    </a>
   </li>
  </ul>
  <h2>
   Resources
  </h2>
  <p>
   <strong>
    man or help
   </strong>
   :
  </p>
  <ul>
   <li>
    <code>
     curl
    </code>
   </li>
  </ul>
  
 </div>
</div>

[--LINK PROJECT--](https://intranet.hbtn.io/projects/265)
</html>