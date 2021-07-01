from models import tech_obj, person_obj, question


"""person_obj images"""
derek_images = []
tori_images = []
libby_images = []
stan_images = []
kristen_images = []

derek_images.append("../assets/images/derek_1.PNG")
derek_images.append("../assets/images/derek_2.PNG")
derek_images.append("../assets/images/derek_3.PNG")

tori_images.append("../assets/images/tori_1.PNG")
tori_images.append("../assets/images/tori_2.PNG")
tori_images.append("../assets/images/tori_3.PNG")

libby_images.append("../assets/images/libby_1.PNG")
libby_images.append("../assets/images/libby_2.PNG")
libby_images.append("../assets/images/libby_3.PNG")

stan_images.append("../assets/images/stan_1.PNG")
stan_images.append("../assets/images/stan_2.PNG")
stan_images.append("../assets/images/stan_3.PNG")

kristen_images.append("../assets/images/kristen_1.PNG")
kristen_images.append("../assets/images/kristen_2.PNG")
kristen_images.append("../assets/images/kristen_3.PNG")

# derek_img = "../assets/images/"
# tori_img = "../assets/images/"
# libby_img = "../assets/images/"
# stan_img = "../assets/images/"
# guillaume_img = "../assets/images/"


"""tech_obj images"""
google_images = []
intranet_images = []
vs_code_images = []
vagrant_images = []
github_images = []

google_images.append("../assets/images/google_1.PNG")
google_images.append("../assets/images/google_2.PNG")
google_images.append("../assets/images/google_3.PNG")

intranet_images.append("../assets/images/intranet_1.PNG")
intranet_images.append("../assets/images/intranet_2.PNG")
intranet_images.append("../assets/images/intranet_3.PNG")

vs_code_images.append("../assets/images/vscode_1.PNG")
vs_code_images.append("../assets/images/vscode_2.PNG")
vs_code_images.append("../assets/images/vscode_3.PNG")

vagrant_images.append("../assets/images/")
vagrant_images.append("../assets/images/")
vagrant_images.append("../assets/images/")

github_images.append("../assets/images/")
github_images.append("../assets/images/")
github_images.append("../assets/images/")



# google_img = "../assets/images/"
# intranet_img = "../assets/images/"
# vs_code_img = "../assets/images/"
# vagrant_img = "../assets/images/"
# github_img = "../assets/images/"


"""question images"""

derekQ_img = ["../assets/images/"]
toriQ_img = ["../assets/images/"]
libbyQ_img = ["../assets/images/"]
googleQ_img = ["../assets/images/"]
intranetQ_img = ["../assets/images/"]
# githubQ_img = "../assets/images/"


"""init persons"""
# def __init__(self, image, pos, name):

persons_list = []

persons_list.append(person_obj(derek_images, (200, 600), "Derek"))
persons_list.append(person_obj(tori_images, (600, 600), "Tori"))
persons_list.append(person_obj(libby_images, (900, 600), "Libby"))
persons_list.append(person_obj(stan_images, (600, 600), "Stan"))
persons_list.append(person_obj(kristen_images, (900, 600), "Kristen"))



"""init tech_objs"""
# def __init__(self, image, pos, name):

tech_obj_list = []

tech_obj_list.append(tech_obj(google_images, (200, 600), "Google"))
tech_obj_list.append(tech_obj(intranet_images, (600, 600), "Intranet"))
tech_obj_list.append(tech_obj(vs_code_images, (900, 600), "VS Code"))
tech_obj_list.append(tech_obj(vagrant_images, (600, 600), "Vagrant"))
tech_obj_list.append(tech_obj(github_images, (900, 600), "Github"))


"""init questions"""

questions_list = []

questions_list.append(question(derekQ_img, (150, 100), persons_list[0].id))
questions_list.append(question(toriQ_img, (150, 100), persons_list[1].id))
questions_list.append(question(googleQ_img, (150, 100), tech_obj_list[0].id))
questions_list.append(question(intranetQ_img, (150, 100), tech_obj_list[1].id))
# questions_list.append(question(derekQ_img, (150, 100), persons_list[0].id))


