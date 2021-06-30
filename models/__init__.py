from models import tech_obj, person_obj, question


"""person_obj images"""

derek_img = "../assets/images/"
tori_img = "../assets/images/"
libby_img = "../assets/images/"
stan_img = "../assets/images/"
guillaume_img = "../assets/images/"


"""tech_obj images"""

google_img = "../assets/images/"
intranet_img = "../assets/images/"
vs_code_img = "../assets/images/"
vagrant_img = "../assets/images/"
github_img = "../assets/images/"


"""question images"""

derekQ_img = "../assets/images/"
toriQ_img = "../assets/images/"
libbyQ_img = "../assets/images/"
googleQ_img = "../assets/images/"
intranetQ_img = "../assets/images/"
githubQ_img = "../assets/images/"


"""init persons"""
# def __init__(self, image, pos, name):

persons_list = []

persons_list.append(person_obj(derek_img, (200, 600), "Derek"))
persons_list.append(person_obj(tori_img, (600, 600), "Tori"))
persons_list.append(person_obj(libby_img, (900, 600), "Libby"))
persons_list.append(person_obj(stan_img, (600, 600), "Stan"))
persons_list.append(person_obj(guillaume_img, (900, 600), "Guillaume"))



"""init tech_objs"""
# def __init__(self, image, pos, name):

tech_obj_list = []

tech_obj_list.append(tech_obj(google_img, (200, 600), "Google"))
tech_obj_list.append(tech_obj(intranet_img, (600, 600), "Intranet"))
tech_obj_list.append(tech_obj(vs_code_img, (900, 600), "VS Code"))
tech_obj_list.append(tech_obj(vagrant_img, (600, 600), "Vagrant"))
tech_obj_list.append(tech_obj(github_img, (900, 600), "Github"))


"""init questions"""

questions_list = []

questions_list.append(question(derekQ_img, (150, 100), persons_list[0].id))
questions_list.append(question(toriQ_img, (150, 100), persons_list[1].id))
questions_list.append(question(googleQ_img, (150, 100), tech_obj_list[0].id))
questions_list.append(question(intranetQ_img, (150, 100), tech_obj_list[1].id))
# questions_list.append(question(derekQ_img, (150, 100), persons_list[0].id))


