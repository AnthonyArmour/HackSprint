from models.objects import tech_obj, person_obj, question
import os

# person_obj images
derek_images = []
derek_images.append(os.path.join("Assets/images/person_objs", "derek_1.PNG"))
derek_images.append(os.path.join("Assets/images/person_objs", "derek_2.PNG"))
derek_images.append(os.path.join("Assets/images/person_objs", "derek_3.PNG"))

tori_images = []
tori_images.append(os.path.join("Assets/images/person_objs", "tori_1.PNG"))
tori_images.append(os.path.join("Assets/images/person_objs", "tori_2.PNG"))
tori_images.append(os.path.join("Assets/images/person_objs", "tori_3.PNG"))

libby_images = []
libby_images.append(os.path.join("Assets/images/person_objs", "libby_1.PNG"))
libby_images.append(os.path.join("Assets/images/person_objs", "libby_2.PNG"))
libby_images.append(os.path.join("Assets/images/person_objs", "libby_3.PNG"))

stan_images = []
stan_images.append(os.path.join("Assets/images/person_objs", "stan_1.PNG"))
stan_images.append(os.path.join("Assets/images/person_objs", "stan_2.PNG"))
stan_images.append(os.path.join("Assets/images/person_objs", "stan_3.PNG"))

stutor_images = []
stutor_images.append(os.path.join("Assets/images/person_objs", "stutor_1.PNG"))
stutor_images.append(os.path.join("Assets/images/person_objs", "stutor_2.PNG"))
stutor_images.append(os.path.join("Assets/images/person_objs", "stutor_3.PNG"))

# tech_obj images
google_images = []
google_images.append(os.path.join("Assets/images/tech_objs", "google_1.PNG"))
google_images.append(os.path.join("Assets/images/tech_objs", "google_2.PNG"))
google_images.append(os.path.join("Assets/images/tech_objs", "google_3.PNG"))

intranet_images = []
intranet_images.append(os.path.join("Assets/images/tech_objs", "intranet_1.PNG"))
intranet_images.append(os.path.join("Assets/images/tech_objs", "intranet_2.PNG"))
intranet_images.append(os.path.join("Assets/images/tech_objs", "intranet_3.PNG"))

vs_code_images = []
vs_code_images.append(os.path.join("Assets/images/tech_objs", "vscode_1.PNG"))
vs_code_images.append(os.path.join("Assets/images/tech_objs", "vscode_2.PNG"))
vs_code_images.append(os.path.join("Assets/images/tech_objs", "vscode_3.PNG"))

vbox_images = []
vbox_images.append(os.path.join("Assets/images/tech_objs", "virtualbox_1.PNG"))
vbox_images.append(os.path.join("Assets/images/tech_objs", "virtualbox_2.PNG"))
vbox_images.append(os.path.join("Assets/images/tech_objs", "virtualbox_3.PNG"))

github_images = []
github_images.append(os.path.join("Assets/images/tech_objs", "github_1.PNG"))
github_images.append(os.path.join("Assets/images/tech_objs", "github_2.PNG"))
github_images.append(os.path.join("Assets/images/tech_objs", "github_3.PNG"))

# question images
derekQ_img = os.path.join("Assets/images/textbox_objs", "text_derek.PNG")
toriQ_img = os.path.join("Assets/images/textbox_objs", "text_tori.PNG")
googleQ_img = os.path.join("Assets/images/textbox_objs", "text_google.PNG")
intranetQ_img = os.path.join("Assets/images/textbox_objs", "text_intranet.PNG")

#init persons(self, image, pos, name):
persons_list = []
persons_list.append(person_obj(derek_images, (200, 600), "Derek"))
persons_list.append(person_obj(tori_images, (600, 600), "Tori"))
persons_list.append(person_obj(libby_images, (900, 600), "Libby"))
persons_list.append(person_obj(stan_images, (600, 600), "Stan"))
persons_list.append(person_obj(stutor_images, (900, 600), "stutor"))


#init tech_objs (self, image, pos, name):
tech_obj_list = []
tech_obj_list.append(tech_obj(google_images, (200, 600), "Google"))
tech_obj_list.append(tech_obj(intranet_images, (600, 600), "Intranet"))
tech_obj_list.append(tech_obj(vs_code_images, (900, 600), "VS Code"))
tech_obj_list.append(tech_obj(vbox_images, (600, 600), "vbox"))
tech_obj_list.append(tech_obj(github_images, (900, 600), "Github"))

# init questions
questions_list = []
questions_list.append(question(derekQ_img, (150, 100), persons_list[0].name))
questions_list.append(question(toriQ_img, (150, 100), persons_list[1].name))
questions_list.append(question(googleQ_img, (150, 100), tech_obj_list[0].name))
questions_list.append(question(intranetQ_img, (150, 100), tech_obj_list[1].name))
