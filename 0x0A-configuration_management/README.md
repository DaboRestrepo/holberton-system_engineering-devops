# 0x0A. Configuration management

<html>
<div class="panel panel-default" id="project-description">
 <div class="panel-body">
  <h2>
   Background Context
  </h2>
  <p>
   <a href="https://youtu.be/ogYLFyp68cI" target="_blank">
    <img alt="" src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2019/6/6a0a8024f2b1c47a9d1e.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220608%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20220608T235801Z&amp;X-Amz-Expires=86400&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=8d5941dc9fa48762be0abf93cfbda6edb4374dc1e1a14f0c11aa67dcd11e3e6c" style=""/>
   </a>
  </p>
  <p>
   When I was working for SlideShare, I worked on an auto-remediation tool called
   <a href="https://engineering.linkedin.com/slideshare/skynet-project-_-monitor-scale-and-auto-heal-system-cloud" target="_blank" title="Skynet">
    Skynet
   </a>
   that monitored, scaled and fixed Cloud infrastructure. I was using a parallel job-execution system called MCollective that allowed me to execute commands to one or multiple servers at the same time. I could apply an action to a selected set of servers by applying a filter such as the server’s hostname or any other metadata we had (server type, server environment…). At some point, a bug was present in my code that sent
   <code>
    nil
   </code>
   to the filter method.
  </p>
  <p>
   There were 2 pieces of bad news:
  </p>
  <ol>
   <li>
    When MCollective receives
    <code>
     nil
    </code>
    as an argument for its filter method, it takes this to mean ‘all servers’
   </li>
   <li>
    The action I sent was to terminate the selected servers
   </li>
  </ol>
  <p>
   I started the parallel job-execution and after some time, I realized that it was taking longer than expected. Looking at logs I realized that I was shutting down SlideShare’s entire document conversion environment. Actually, 75% of all our conversion infrastructure servers had been shut down, resulting in users not able to convert their PDFs, powerpoints, and videos… Pretty bad!
  </p>
  <p>
   Thanks to Puppet, we were able to restore our infrastructure to normal operation in under 1H, pretty impressive. Imagine if we had to do everything manually: launching the servers, configuring and linking them, importing application code, starting every process, and obviously, fixing all the bugs (you should know by now that complicated infrastructure always goes sideways)…
  </p>
  <p>
   Obviously writing Puppet code for your infrastructure requires an investment of time and energy, but in the long term, it is for sure a must-have.
  </p>
  <p>
   <img alt="" src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/292/4i8il3B.gif" style=""/>
  </p>
  <p>
   That was me ^_^‘:
   <a href="https://twitter.com/devopsreact/status/836971570136375296" target="_blank" title="https://twitter.com/devopsreact/status/836971570136375296">
    https://twitter.com/devopsreact/status/836971570136375296
   </a>
  </p>
  <h2>
   Resources
  </h2>
  <p>
   <strong>
    Read or watch
   </strong>
   :
  </p>
  <ul>
   <li>
    <a href="https://www.digitalocean.com/community/tutorials/an-introduction-to-configuration-management" target="_blank" title="Intro to Configuration Management">
     Intro to Configuration Management
    </a>
   </li>
   <li>
    <a href="https://puppet.com/docs/puppet/5.5/types/file.html" target="_blank" title="Puppet resource type: file">
     Puppet resource type: file
    </a>
    (
    <em>
     check “Resource types” for all manifest types in the left menu
    </em>
    )
   </li>
   <li>
    <a href="https://puppet.com/blog/puppets-declarative-language-modeling-instead-of-scripting/" target="_blank" title="Puppet's Declarative Language: Modeling Instead of Scripting">
     Puppet’s Declarative Language: Modeling Instead of Scripting
    </a>
   </li>
   <li>
    <a href="http://puppet-lint.com/" target="_blank" title="Puppet lint">
     Puppet lint
    </a>
   </li>
   <li>
    <a href="https://github.com/voxpupuli/puppet-mode" target="_blank" title="Puppet emacs mode">
     Puppet emacs mode
    </a>
   </li>
  </ul>
  
 </div>
</div>

[--LINK PROJECT--](https://intranet.hbtn.io/projects/292)
</html>