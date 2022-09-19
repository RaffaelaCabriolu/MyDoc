import link

link_name = "ganglia_interface"
user_text = "ganglia"                    
url = "http://bird.phys.ntnu.no/ganglia/?r=4hr&cs=&ce=&m=load_one&tab=ch&vn=&hide-hf=false&hreg%5B%5D=phys"

link.xref_links.update({link_name: (user_text, url)})


#link_name = "Unique Link Name"
#user_text = "Link text the user sees"
#url = "URL link address"

#link.xref_links.update({link_name: (user_text, url)})
