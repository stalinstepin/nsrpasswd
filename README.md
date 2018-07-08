# NetWorker - nsrpasswd
**`nsrpasswd`** is a tool that is built to automate the NMC password reset process. This will help the customers to reset the password without having to touch any file and to find the base64 encoded format of the password which needs to be added to the JSON file. This will make the reset process a lot easier and error free.

You can view the same information from **[DELL EMC Knowledgebase](https://support.emc.com/kb/518882).**

---

# How do I use it?
* Download the Python script and make an executable file:
* Place the executable under **/usr/sbin** for Linux and **C:\Program Files\EMC NetWorker\nsr\bin** for Windows on NetWorker Server.
* Execute the binary by running the following command from terminal for Linux: **`/usr/sbin/nsrpasswd`**
* Navigate to **C:\Program Files\EMC NetWorker\nsr\bin** and execute the binary by running the following command from command prompt for Windows: **nsrpasswd**
* From here all that you need to provide is the password and the rest is taken care by the script.

---


# Here is the list of tasks that the script performs:

* Converts the provided plain text password to base64 encoded string.
* Makes a copy of the JSON file and keeps in buffer which will be used for password reset. 
* Replaces the password in the JSON file and saves the file under **'C:\Program Files\EMC NetWorker\nsr\authc-server\tomcat\conf\authc-local-config.json'** on Windows and **'/nsr/authc/conf/authc-local-config.json'** on Linux.
* Restarts the NetWorker services to the changes to the applied to the authc Database.


---

# Screenshots:

![](https://3.bp.blogspot.com/-z7oEfY7u_SY/W0C_y-h8ZrI/AAAAAAAAAdQ/0xavmT2txlAigmZklmsB7VpZ0HorswLiwCLcBGAs/s1600/nsrpasswd_windows.png)
![](https://1.bp.blogspot.com/-LB--jn9k8Uo/W0DT8pjm-_I/AAAAAAAAAdo/g7ECwelhWvgFFC_Yt5JysPDIM7VnE2ABACLcBGAs/s1600/nsrpasswd_Linux2.PNG)
![](https://2.bp.blogspot.com/-o0Vy9MXqFaY/W0DT8iiODRI/AAAAAAAAAds/69LLtO7Q68Mh4kuMDFKblSi2JlYz9zwFQCLcBGAs/s1600/nsrpasswd_Linux1.PNG)
