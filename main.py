from crypt import methods
import json
from starlette.applications import Starlette
from starlette.routing import Route
from starlette.requests import Request
from starlette.responses import JSONResponse
from database import Session
from models import applicant, address, education, experience, skills, projects, social
from datetime import datetime
from sqlalchemy import desc
from validation import BasicDetailsValid
from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware

middleware = [Middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"])]
data_table = Session()


def create_primary(primary_data):
    new_primary = applicant(**primary_data)

    try:
        data_table.add(new_primary)
        data_table.commit()
        data_table.refresh(new_primary)

    except Exception as e:
        print(e)


async def create_primary_details(request: Request):
    if request.method == "POST":
        primary_data = await request.json()
        create_primary(primary_data)
        return JSONResponse({"data": primary_data}, status_code=201)


async def update_primary_details(request: Request):
    id = request.path_params.get("person_id")
    update_details = data_table.query(applicant).filter(
        applicant.basic_details_id == id
    )
    if request.method == "PUT":
        try:
            update_data = await request.json()
            update_details.update(update_data, synchronize_session=False)
            data_table.commit()
        except Exception as e:
            print(e)
    return JSONResponse({"data": "update_data"}, status_code=201)


async def get_allprimary(request):
    details = (
        data_table.query(applicant).order_by(applicant.basic_details_id.desc()).all()
    )
    content = [
        {k: v for k, v in vars(detail).items() if k != "_sa_instance_state"}
        for detail in details
    ]
    content = [
        {k: str(v) if k == "date_applied" else v for k, v in cont.items()}
        for cont in content
    ]

    print(content)
    return JSONResponse({"data": content})


async def delete_primary(request):
    id = request.path_params.get("person_id")
    delete_data = data_table.query(applicant).filter(applicant.basic_details_id == id)
    print(delete_data)
    delete_data.delete()
    data_table.commit()
    return JSONResponse({"data": "deleted"}, status_code=200)


def create_address(request, new_address):
    new_address["basic_details_id"] = request.path_params.get("person_id")
    new_address = address(**new_address)

    try:
        data_table.add(new_address)
        data_table.commit()
        data_table.refresh(new_address)

    except Exception as e:
        print(e)


async def create_address_details(request: Request):
    if request.method == "POST":
        address_data = await request.json()
        create_address(request, address_data)
        return JSONResponse({"data": address_data}, status_code=201)


async def update_address_details(request: Request):
    id = request.path_params.get("person_id")
    update_details = data_table.query(address).filter(address.address_id == id)
    if request.method == "PUT":
        try:
            update_data = await request.json()
            update_details.update(update_data, synchronize_session=False)
            data_table.commit()
        except Exception as e:
            print(e)
    return JSONResponse({"data": "update_data"}, status_code=201)


async def delete_address(request):
    id = request.path_params.get("person_id")
    delete_data = data_table.query(address).filter(address.address_id == id)
    print(delete_data)
    delete_data.delete()
    data_table.commit()
    return JSONResponse({"data": "deleted"}, status_code=200)


async def get_alladdress(request):
    details = data_table.query(address).all()
    content = [
        {k: v for k, v in vars(address).items() if k != "_sa_instance_state"}
        for address in details
    ]
    print(content)
    return JSONResponse({"data": content})


def create_education(request, new_education):
    new_education["basic_details_id"] = request.path_params.get("person_id")
    new_education = education(**new_education)

    try:
        data_table.add(new_education)
        data_table.commit()
        data_table.refresh(new_education)
    except Exception as e:
        print(e)


async def create_education_details(request: Request):
    if request.method == "POST":
        education_data = await request.json()
        education_data["passing_year"] = datetime.strptime(
            education_data["passing_year"], "%Y-%m-%d"
        ).date()
        print(type(education_data["passing_year"]))
        create_education(request, education_data)
        return JSONResponse({"data": "education_data"})


async def update_education_details(request: Request):
    id = request.path_params.get("person_id")
    update_details = data_table.query(education).filter(education.education_id == id)
    if request.method == "PUT":
        try:
            update_data = await request.json()
            update_details.update(update_data, synchronize_session=False)
            data_table.commit()
        except Exception as e:
            print(e)
    return JSONResponse({"data": "update_data"}, status_code=201)


async def delete_education(request):
    id = request.path_params.get("person_id")
    delete_data = data_table.query(education).filter(education.education_id == id)
    print(delete_data)
    delete_data.delete()
    data_table.commit()
    return JSONResponse({"data": "deleted"}, status_code=200)


async def get_alleducation(request):
    details = data_table.query(education).all()
    content = [
        {k: v for k, v in vars(education).items() if k != "_sa_instance_state"}
        for education in details
    ]
    print(content)
    return JSONResponse({"data": content})


def create_experience(request, new_experience):
    new_experience["basic_details_id"] = request.path_params.get("person_id")
    new_experience = experience(**new_experience)

    try:
        data_table.add(new_experience)
        data_table.commit()
        data_table.refresh(new_experience)

    except Exception as e:
        print(e)


async def create_experience_details(request: Request):
    if request.method == "POST":
        experience_data = await request.json()
        create_experience(request, experience_data)
        return JSONResponse({"data": experience_data}, status_code=201)


async def update_experience_details(request: Request):
    id = request.path_params.get("person_id")
    update_details = data_table.query(experience).filter(experience.experience_id == id)
    if request.method == "PUT":
        try:
            update_data = await request.json()
            update_details.update(update_data, synchronize_session=False)
            data_table.commit()
        except Exception as e:
            print(e)
    return JSONResponse({"data": "update_data"}, status_code=201)


async def delete_experience(request):
    id = request.path_params.get("person_id")
    delete_data = data_table.query(experience).filter(experience.experience_id == id)
    print(delete_data)
    delete_data.delete()
    data_table.commit()
    return JSONResponse({"data": "deleted"}, status_code=200)


async def get_allexperience(request):
    details = data_table.query(experience).all()
    content = [
        {k: v for k, v in vars(experience).items() if k != "_sa_instance_state"}
        for experience in details
    ]
    print(content)
    return JSONResponse({"data": content})


def create_skill(request, new_skill):
    new_skill["basic_details_id"] = request.path_params.get("person_id")
    new_skill = skills(**new_skill)

    try:
        data_table.add(new_skill)
        data_table.commit()
        data_table.refresh(new_skill)

    except Exception as e:
        print(e)


async def create_skill_details(request: Request):
    if request.method == "POST":
        skill_data = await request.json()
        create_skill(request, skill_data)
        return JSONResponse({"data": skill_data}, status_code=201)


async def update_skill_details(request: Request):
    id = request.path_params.get("person_id")
    update_details = data_table.query(skills).filter(skills.skill_id == id)
    if request.method == "PUT":
        try:
            update_data = await request.json()
            update_details.update(update_data, synchronize_session=False)
            data_table.commit()
        except Exception as e:
            print(e)
    return JSONResponse({"data": "update_data"}, status_code=201)


async def delete_skill(request):
    id = request.path_params.get("person_id")
    delete_data = data_table.query(skills).filter(skills.skill_id == id)
    print(delete_data)
    delete_data.delete()
    data_table.commit()
    return JSONResponse({"data": "deleted"}, status_code=200)


async def get_allskill(request):
    details = data_table.query(skills).all()
    content = [
        {k: v for k, v in vars(skill).items() if k != "_sa_instance_state"}
        for skill in details
    ]
    print(content)
    return JSONResponse({"data": content})


def create_project(request, new_project):
    new_project["basic_details_id"] = request.path_params.get("person_id")
    new_project = projects(**new_project)

    try:
        data_table.add(new_project)
        data_table.commit()
        data_table.refresh(new_project)

    except Exception as e:
        print(e)


async def create_project_details(request: Request):
    if request.method == "POST":
        project_data = await request.json()
        create_project(request, project_data)
        return JSONResponse({"data": project_data}, status_code=201)


async def update_project_details(request: Request):
    id = request.path_params.get("person_id")
    update_details = data_table.query(projects).filter(projects.project_id == id)
    if request.method == "PUT":
        try:
            update_data = await request.json()
            update_details.update(update_data, synchronize_session=False)
            data_table.commit()
        except Exception as e:
            print(e)
    return JSONResponse({"data": "update_data"}, status_code=201)


async def delete_project(request):
    id = request.path_params.get("person_id")
    delete_data = data_table.query(projects).filter(projects.project_id == id)
    print(delete_data)
    delete_data.delete()
    data_table.commit()
    return JSONResponse({"data": "deleted"}, status_code=200)


async def get_allproject(request):
    details = data_table.query(projects).all()
    content = [
        {k: v for k, v in vars(project).items() if k != "_sa_instance_state"}
        for project in details
    ]
    print(content)
    return JSONResponse({"data": content})


def create_social(request, new_social):
    new_social["basic_details_id"] = request.path_params.get("person_id")
    new_social = social(**new_social)

    try:
        data_table.add(new_social)
        data_table.commit()
        data_table.refresh(new_social)

    except Exception as e:
        print(e)


async def create_social_details(request: Request):
    if request.method == "POST":
        social_data = await request.json()
        create_social(request, social_data)
        return JSONResponse({"data": social_data}, status_code=201)


async def update_social_details(request: Request):
    id = request.path_params.get("person_id")
    update_details = data_table.query(social).filter(social.social_id == id)
    if request.method == "PUT":
        try:
            update_data = await request.json()
            update_details.update(update_data, synchronize_session=False)
            data_table.commit()
        except Exception as e:
            print(e)
    return JSONResponse({"data": "update_data"}, status_code=201)


async def delete_social(request):
    id = request.path_params.get("person_id")
    delete_data = data_table.query(social).filter(social.social_id == id)
    print(delete_data)
    delete_data.delete()
    data_table.commit()
    return JSONResponse({"data": "deleted"}, status_code=200)


async def get_allsocial(request):
    details = data_table.query(social).all()
    content = [
        {k: v for k, v in vars(social).items() if k != "_sa_instance_state"}
        for social in details
    ]
    print(content)
    return JSONResponse({"data": content})


# functons to be used to get the individual resume


def socm(request, id):
    content = data_table.query(social).filter(social.basic_details_id == id).all()
    content = [
        {k: v for k, v in vars(social).items() if k != "_sa_instance_state"}
        for social in content
    ]
    return content


def prim(request, id):
    content = (
        data_table.query(applicant).filter(applicant.basic_details_id == id).first()
    )
    print(content)
    content = [{k: v for k, v in vars(content).items() if k != "_sa_instance_state"}]
    content = [
        {k: str(v) if k == "date_applied" else v for k, v in cont.items()}
        for cont in content
    ]
    return content


def adr(request, id):
    content = data_table.query(address).filter(address.basic_details_id == id).all()
    print(content)
    content = [
        {k: v for k, v in vars(details).items() if k != "_sa_instance_state"}
        for details in content
    ]
    return content


def educ(request, id):
    content = data_table.query(education).filter(education.basic_details_id == id).all()
    content = [
        {k: v for k, v in vars(education).items() if k != "_sa_instance_state"}
        for education in content
    ]
    content = [
        {k: str(v) if k == "passing_year" else v for k, v in cont.items()}
        for cont in content
    ]
    return content


def expr(request, id):
    content = (
        data_table.query(experience).filter(experience.basic_details_id == id).all()
    )
    content = [
        {k: v for k, v in vars(experience).items() if k != "_sa_instance_state"}
        for experience in content
    ]
    content = [
        {k: str(v) if k in ["start_date", "end_date"] else v for k, v in cont.items()}
        for cont in content
    ]
    return content


def skl(request, id):
    content = data_table.query(skills).filter(skills.basic_details_id == id).all()
    content = [
        {k: v for k, v in vars(skill).items() if k != "_sa_instance_state"}
        for skill in content
    ]
    return content


def pro(request, id):
    content = data_table.query(projects).filter(projects.basic_details_id == id).all()
    content = [
        {k: v for k, v in vars(project).items() if k != "_sa_instance_state"}
        for project in content
    ]
    return content


# to get individual resume
async def get_individual_resume(request):
    id = request.path_params.get("person_id")

    if request.method == "GET":
        get_primary = prim(request, id)
        get_address = adr(request, id)
        get_education = educ(request, id)
        get_experience = expr(request, id)
        get_skill = skl(request, id)
        get_social = socm(request, id)
        get_project = pro(request, id)

        print()

        return JSONResponse(
            {
                "prim": get_primary,
                "adrs": get_address,
                "edu": get_education,
                "exp": get_experience,
                "skl": get_skill,
                "sm": get_social,
                "prjct": get_project,
            }
        )
    if request.method == "PUT":
        id = request.path_params.get("person_id")
        update_data = await request.json()
        primary = update_data.pop("prim")
        addres = update_data.pop("adrs")
        educationn = update_data.pop("edu")
        expe = update_data.pop("exp")
        project = update_data.pop("prjct")
        skill = update_data.pop("skl")
        social_media = update_data.pop("sm")

        try:
            for pr in primary:
                primary_details_db = data_table.query(applicant).filter(
                    applicant.basic_details_id == id
                )
                primary_details_db.update(pr, synchronize_session=False)
                data_table.commit()
            for ad in addres:
                if "address_id" in ad.keys():
                    address_details_db = data_table.query(address).filter(
                        (address.basic_details_id == id)
                        & (address.address_id == ad["address_id"])
                    )
                    address_details_db.update(ad, synchronize_session=False)
                    data_table.commit()
                else:
                    print("add")
                    ad["basic_details_id"] = id
                    new_address = address(**ad)
                    data_table.add(new_address)
                    data_table.commit()
                    house_name = [sub["House_name"] for sub in addres]
                    house_name_db = data_table.query(address.House_name).filter(
                        (address.basic_details_id == id)
                    )
                    house_name_from_table = [lis[0] for lis in house_name_db]
                    for name in house_name_from_table:
                        if name not in house_name:
                            data_table.query(address).filter(
                                address.House_name == name
                            ).delete()
                            data_table.commit()
            for ed in educationn:
                if ed.get("education_id", ""):
                    education_details_db = data_table.query(education).filter(
                        (education.basic_details_id == id)
                        & (education.education_id == ed["education_id"])
                    )
                    education_details_db.update(ed, synchronize_session=False)
                    data_table.commit()
                else:
                    print("add")
                    ed["basic_details_id"] = id
                    new_education = education(**ed)
                    data_table.add(new_education)
                    data_table.commit()
            qualification = [sub["Qualification"] for sub in educationn]
            qualification_db = data_table.query(education.Qualification).filter(
                (education.basic_details_id == id)
            )
            qualification_from_table = [lis[0] for lis in qualification_db]
            for q in qualification_from_table:
                if q not in qualification:
                    delete_data = data_table.query(education).filter(
                        education.Qualification == q
                    )
                    delete_data.delete()
                    data_table.commit()

            for ex in expe:
                if ex.get("experience_id", ""):
                    experience_details_db = data_table.query(experience).filter(
                        (experience.basic_details_id == id)
                        & (experience.experience_id == ex["experience_id"])
                    )
                    experience_details_db.update(ex, synchronize_session=False)
                    data_table.commit()
                else:
                    print("add")
                    ex["basic_details_id"] = id
                    new_experience = experience(**ex)
                    data_table.add(new_experience)
                    data_table.commit()
            roles = [sub["role"] for sub in expe]
            role_db = data_table.query(experience.role).filter(
                (experience.basic_details_id == id)
            )
            role_from_table = [lis[0] for lis in role_db]
            for e in role_from_table:
                if e not in roles:
                    delete_data = data_table.query(experience).filter(
                        experience.role == e
                    )
                    delete_data.delete()
                    data_table.commit()

            for pr in project:
                if pr.get("project_id", ""):
                    project_details_db = data_table.query(projects).filter(
                        (projects.basic_details_id == id)
                        & (projects.project_id == pr["project_id"])
                    )
                    project_details_db.update(pr, synchronize_session=False)
                    data_table.commit()
                else:
                    print("add")
                    pr["basic_details_id"] = id
                    new_project = projects(**pr)
                    data_table.add(new_project)
                    data_table.commit()
            proj = [sub["project_title"] for sub in project]
            proj_db = data_table.query(projects.project_title).filter(
                projects.basic_details_id == id
            )
            proje_from_table = [lis[0] for lis in proj_db]
            for p in proje_from_table:
                if p not in proj:
                    delete_data = data_table.query(projects).filter(
                        projects.project_title == p
                    )
                    delete_data.delete()
                    data_table.commit()

            for sk in skill:
                if sk.get("skill_id", ""):
                    skill_details_db = data_table.query(skills).filter(
                        (skills.basic_details_id == id)
                        & (skills.skill_id == sk["skill_id"])
                    )
                    skill_details_db.update(sk, synchronize_session=False)
                    data_table.commit()
                else:
                    print("Add")
                    sk["basic_details_id"] = id
                    new_skill = skills(**sk)
                    data_table.add(new_skill)
                    data_table.commit()
            ski = [sub["skill_name"] for sub in skill]
            skill_db = data_table.query(skills.skill_name).filter(
                (skills.basic_details_id == id)
            )
            skill_from_table = [lis[0] for lis in skill_db]
            for s in skill_from_table:
                if s not in ski:
                    delete_skl = data_table.query(skills).filter(skills.skill_name == s)
                    delete_skl.delete()
                    data_table.commit()

            for sm in social_media:
                if sm.get("social_id", ""):
                    social_media_db = data_table.query(social).filter(
                        (social.basic_details_id == id)
                        & (social.social_id == sm["social_id"])
                    )
                    social_media_db.update(sm, synchronize_session=False)
                    data_table.commit()
                else:
                    sm["basic_details_id"] = id
                    new_social = social(**sm)
                    data_table.add(new_social)
                    data_table.commit
            smedia = [sub["platform"] for sub in social_media]
            social_db = data_table.query(social.platform).filter(
                (social.basic_details_id == id)
            )
            social_from_table = [lis[0] for lis in social_db]
            for som in social_from_table:
                if som not in smedia:
                    delete_social = data_table.query(social).filter(
                        social.platform == som
                    )
                    delete_social.delete()
                    data_table.commit()

        except Exception as e:
            print("error: ", e)
    return JSONResponse({"data": "edited successfully"})


async def new_resume(request):
    if request.method == "POST":
        primary_details_data = await request.json()

        address_data = primary_details_data.pop("address_details")
        education_data = primary_details_data.pop("education_details")
        experience_data = primary_details_data.pop("experience_details")
        skill_data = primary_details_data.pop("skill_details")
        project_data = primary_details_data.pop("project_details")
        social_data = primary_details_data.pop("social_details")

        new_primary_details_data = applicant(**primary_details_data)
        try:
            BasicDetailsValid.from_orm(new_primary_details_data)
            data_table.add(new_primary_details_data)
            data_table.commit()
            data_table.refresh(new_primary_details_data)
        except Exception as e:
            return JSONResponse({"error_message": f"{e}"})

        basic_details_id = data_table.query(applicant.basic_details_id).all()
        greater_basic_id = max([i for ik in basic_details_id for i in ik])
        print(greater_basic_id)

        for adrs in address_data:
            adrs["basic_details_id"] = greater_basic_id
        print("Address: ", address_data)
        new_address_details = [address(**i) for i in address_data]
        print("New Address :", address_data)
        try:
            data_table.add_all(new_address_details)
            data_table.commit()
        except Exception as e:
            print("error", e)

        for educ in education_data:
            educ["basic_details_id"] = greater_basic_id
            print("Education :", education_data)
            print("New education: ", education_data)
            try:
                new_education_details = [education(**i) for i in education_data]
                data_table.add_all(new_education_details)
                data_table.commit()
            except Exception as e:
                print("error", e)

        for expe in experience_data:
            expe["basic_details_id"] = greater_basic_id
            print("Education :", experience_data)
            print("New experience :", experience_data)
            try:
                new_experience_details = [experience(**i) for i in experience_data]
                data_table.add_all(new_experience_details)
                data_table.commit()
            except Exception as e:
                print("error", e)

        for skll in skill_data:
            skll["basic_details_id"] = greater_basic_id
            print("Skills :", skill_data)

        try:
            new_skill_details = [skills(**i) for i in skill_data]
            data_table.add_all(new_skill_details)
            data_table.commit()
        except Exception as e:
            print("error", e)

        for proj in project_data:
            proj["basic_details_id"] = greater_basic_id
            print("Projects :", project_data)

            try:
                new_project_details = [projects(**i) for i in project_data]
                data_table.add_all(new_project_details)
                data_table.commit()
            except Exception as e:
                print("error", e)

        for soc in social_data:
            soc["basic_details_id"] = greater_basic_id
            print("Social media :", social_data)
            print("New social media :", social_data)
            try:
                new_socila_details = [social(**i) for i in social_data]
                data_table.add_all(new_socila_details)
                data_table.commit()
            except Exception as e:
                print("error", e)
    return JSONResponse({"data": "added"}, status_code=200)


async def search(request: Request):
    search_key = request.path_params.get("name")
    search_name = (
        data_table.query(applicant)
        .filter((applicant.name.contains(search_key)) | (applicant.email == search_key))
        .all()
    )
    content = [
        {k: v for k, v in vars(search_nam).items() if k != "_sa_instance_state"}
        for search_nam in search_name
    ]
    content = [
        {k: str(v) if k == "date_applied" else v for k, v in cont.items()}
        for cont in content
    ]

    return JSONResponse({"data": content}, status_code=200)


routes = [
    Route(
        "/create_primary_details",
        endpoint=create_primary_details,
        methods=["GET", "POST"],
    ),
    Route(
        "/delete_primary/{person_id:int}/", endpoint=delete_primary, methods=["DELETE"]
    ),
    Route(
        "/update_primary_details/{person_id:int}/",
        endpoint=update_primary_details,
        methods=["GET", "PUT"],
    ),
    Route("/get_allprimary", endpoint=get_allprimary),
    Route(
        "/create_address_details/{person_id:int}",
        endpoint=create_address_details,
        methods=["GET", "POST"],
    ),
    Route(
        "/update_address_details/{person_id:int}",
        endpoint=update_address_details,
        methods=["GET", "PUT"],
    ),
    Route(
        "/delete_address/{person_id:int}/", endpoint=delete_address, methods=["DELETE"]
    ),
    Route("/get_alladdress", endpoint=get_alladdress),
    Route(
        "/create_education_details/{person_id:int}/",
        endpoint=create_education_details,
        methods=["GET", "POST"],
    ),
    Route(
        "/update_educational_details/{person_id:int}/",
        endpoint=update_education_details,
        methods=["GET", "PUT"],
    ),
    Route(
        "/delete_education/{person_id:int}/",
        endpoint=delete_education,
        methods=["DELETE"],
    ),
    Route("/get_alleducation", endpoint=get_alleducation),
    Route(
        "/create_experience_details/{person_id:int}/",
        endpoint=create_experience_details,
        methods=["GET", "POST"],
    ),
    Route(
        "/update_experience_details/{person_id:int}",
        endpoint=update_experience_details,
        methods=["GET", "PUT"],
    ),
    Route(
        "/delete_experience/{person_id:int}/",
        endpoint=delete_experience,
        methods=["DELETE"],
    ),
    Route("/get_allexpereince", endpoint=get_allexperience),
    Route(
        "/create_skill_details/{person_id:int}/",
        endpoint=create_skill_details,
        methods=["GET", "POST"],
    ),
    Route(
        "/update_skill_details/{person_id:int}/",
        endpoint=update_skill_details,
        methods=["GET", "PUT"],
    ),
    Route("/delete_skill/{person_id:int}/", endpoint=delete_skill, methods=["DELETE"]),
    Route("/get_allskill", endpoint=get_allskill),
    Route(
        "/create_project_details/{person_id}/",
        endpoint=create_project_details,
        methods=["GET", "POST"],
    ),
    Route(
        "/update_project_details/{person_id:int}/",
        endpoint=update_project_details,
        methods=["GET", "PUT"],
    ),
    Route(
        "/delete_project/{person_id:int}/", endpoint=delete_project, methods=["DELETE"]
    ),
    Route("/get_allproject", endpoint=get_allproject),
    Route(
        "/create_social_details/{person_id}/",
        endpoint=create_social_details,
        methods=["GET", "POST"],
    ),
    Route(
        "/update_social_details/{person_id:int}/",
        endpoint=update_social_details,
        methods=["GET", "PUT"],
    ),
    Route(
        "/delete_social/{person_id:int}/", endpoint=delete_social, methods=["DELETE"]
    ),
    Route("/get_allsocial", endpoint=get_allsocial),
    Route(
        "/get_individual_resume/{person_id:int}",
        endpoint=get_individual_resume,
        methods=["GET", "PUT"],
    ),
    Route("/new_resume", endpoint=new_resume, methods=["POST"]),
    Route("/search/{name:str}/", endpoint=search, methods=["GET"]),
]
app = Starlette(routes=routes, middleware=middleware)
