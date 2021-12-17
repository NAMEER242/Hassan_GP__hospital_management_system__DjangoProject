from django.core import serializers
from django.http import HttpResponse
from rest_framework.decorators import api_view
from .models import *


@api_view(['Post'])
def createAccount(request):
    AccountType = str(request.query_params.get('type'))
    if AccountType == "doc":
        createDocAccount(request)

    elif AccountType == "pat":
        createPatAccount(request)

    elif AccountType == "emp":
        createEmployeeAccount(request)

    return HttpResponse("hi")


def createDocAccount(request):
    name = str(request.query_params.get('name'))
    age = int(request.query_params.get('age'))
    certificate = (request.query_params.get('cer'))
    image = (request.query_params.get('img'))
    specialization = str(request.query_params.get('spc'))
    country = str(request.query_params.get('con'))
    phone = str(request.query_params.get('phone'))
    # Account Creation inputs...
    email = str(request.query_params.get('email'))
    password = str(request.query_params.get('pass'))

    username = "doc" + str(len(CustomUser.objects.all()) + 1)
    CustomUser.objects.create_user(
        username,
        email,
        password,
        first_name=name,
    )

    Doctor.objects.create(
        name=name,
        age=age,
        certification_image=certificate,
        image=image,
        specialization=specialization,
        country=country,
        phone_number=phone,
        ID=CustomUser.objects.get(username=username).ID
    )


def createPatAccount(request):
    name = str(request.query_params.get('name'))
    age = int(request.query_params.get('age'))
    patientAddress = str(request.query_params.get('address'))
    notes = str(request.query_params.get('notes'))
    # Account Creation inputs...
    email = str(request.query_params.get('email'))
    password = str(request.query_params.get('pass'))

    username = "pat" + str(len(CustomUser.objects.all()) + 1)
    CustomUser.objects.create_user(
        username,
        email,
        password,
        first_name=name,
    )

    Patient.objects.create(
        name=name,
        age=age,
        patientAddress=patientAddress,
        notes=notes,
        ID=CustomUser.objects.get(username=username).ID
    )


def createEmployeeAccount(request):
    name = str(request.query_params.get('name'))
    age = int(request.query_params.get('age'))
    job = str(request.query_params.get('job'))
    phone = str(request.query_params.get('phone'))
    salary = str(request.query_params.get('salary'))
    # Account Creation inputs...
    email = str(request.query_params.get('email'))
    password = str(request.query_params.get('pass'))

    username = "emp" + str(len(CustomUser.objects.all()) + 1)
    CustomUser.objects.create_user(
        username,
        email,
        password,
        first_name=name,
    )

    Employee.objects.create(
        name=name,
        age=age,
        job=job,
        phone_number=phone,
        salary=salary,
        ID=CustomUser.objects.get(username=username).ID
    )


@api_view(['GET'])
def getDoctorsInformation(request):
    doctors = None
    if str(list(request.query_params.keys())[0]) == "lvl":
        level = int(request.query_params.get('lvl'))
        doctors = Doctor.objects.all()[level * 20:(level + 1) * 20]
    elif str(list(request.query_params.keys())[0]) == "len":
        length = int(request.query_params.get('len'))
        doctors = Doctor.objects.all()[0:length]

    return HttpResponse(toJson(doctors), content_type="application/json")


@api_view(['GET'])
def getPatientsInformation(request):
    patients = None
    if str(list(request.query_params.keys())[0]) == "lvl":
        level = int(request.query_params.get('lvl'))
        patients = Patient.objects.all()[level * 20:(level + 1) * 20]
    elif str(list(request.query_params.keys())[0]) == "len":
        length = int(request.query_params.get('len'))
        patients = Patient.objects.all()[0:length]

    return HttpResponse(toJson(patients), content_type="application/json")


@api_view(['GET'])
def getEmployeesInformation(request):
    employees = None
    if str(list(request.query_params.keys())[0]) == "lvl":
        level = int(request.query_params.get('lvl'))
        employees = Employee.objects.all()[level * 20:(level + 1) * 20]
    elif str(list(request.query_params.keys())[0]) == "len":
        length = int(request.query_params.get('len'))
        employees = Employee.objects.all()[0:length]

    return HttpResponse(toJson(employees), content_type="application/json")


def toJson(objects):
    tmpJson = serializers.serialize("json", objects)
    res = []
    for j in eval(tmpJson):
        res.append(j["fields"])
    return res


@api_view(['DELETE'])
def delUser(request):
    if request.query_params.get('userType') == "doc":
        docId = int(request.query_params.get('id'))
        doc = Doctor.objects.get(ID=docId)
        doc.delete()
        user = CustomUser.objects.get(ID=docId)
        user.delete()
    elif request.query_params.get('userType') == "emp":
        empId = int(request.query_params.get('id'))
        emp = Employee.objects.get(ID=empId)
        emp.delete()
        user = CustomUser.objects.get(ID=empId)
        user.delete()
    elif request.query_params.get('userType') == "pat":
        patId = int(request.query_params.get('id'))
        pat = Patient.objects.get(ID=patId)
        pat.delete()
        user = CustomUser.objects.get(ID=patId)
        user.delete()
    else:
        return HttpResponse("Type error '" + request.query_params.get('userType') + "'")

    return HttpResponse("Done!!")


@api_view(['PUT'])
def updateDoc(request):
    userID = int(request.query_params.get('id'))
    name = str(request.query_params.get('name'))
    age = int(request.query_params.get('age'))
    certificate = (request.query_params.get('cer'))
    image = (request.query_params.get('img'))
    specialization = str(request.query_params.get('spc'))
    country = str(request.query_params.get('con'))
    phone = str(request.query_params.get('phone'))
    # Account Update inputs...
    password = str(request.query_params.get('pass'))

    user = CustomUser.objects.get(ID=userID)
    user.set_password(password)
    user.first_name = name
    user.save()

    doc = Doctor.objects.get(ID=userID)
    doc.name = name
    doc.age = age
    doc.certification_image = certificate
    doc.image = image
    doc.specialization = specialization
    doc.country = country
    doc.phone_number = phone
    doc.save()

    return HttpResponse("Updated!!")


@api_view(['PUT'])
def updatePat(request):
    userID = int(request.query_params.get('id'))
    name = str(request.query_params.get('name'))
    age = int(request.query_params.get('age'))
    patientAddress = str(request.query_params.get('address'))
    notes = str(request.query_params.get('notes'))
    # Account Creation inputs...
    password = str(request.query_params.get('pass'))

    user = CustomUser.objects.get(ID=userID)
    user.set_password(password)
    user.first_name = name
    user.save()

    doc = Patient.objects.get(ID=userID)
    doc.name = name
    doc.age = age
    doc.patientAddress = patientAddress
    doc.notes = notes
    doc.save()

    return HttpResponse("Updated!!")


@api_view(['PUT'])
def updateEmp(request):
    userID = int(request.query_params.get('id'))
    name = str(request.query_params.get('name'))
    age = int(request.query_params.get('age'))
    job = str(request.query_params.get('job'))
    phone = str(request.query_params.get('phone'))
    salary = str(request.query_params.get('salary'))
    # Account Creation inputs...
    password = str(request.query_params.get('pass'))

    user = CustomUser.objects.get(ID=userID)
    user.set_password(password)
    user.first_name = name
    user.save()

    doc = Employee.objects.get(ID=userID)
    doc.name = name
    doc.age = age
    doc.job = job
    doc.salary = salary
    doc.phone_number = phone
    doc.save()

    return HttpResponse("Updated!!")


@api_view(['POST'])
def createReservation(request):
    PID = str(request.query_params.get('pid'))
    DID = str(request.query_params.get('did'))
    gender = str(request.query_params.get('gender'))
    reservationDate = int(request.query_params.get('date'))

    pat = Patient.objects.get(ID=PID)

    Reservation.objects.create(
        PID=PID,
        DID=DID,
        P_name=pat.name,
        P_age=pat.age,
        gender=gender,
        reservations_date=reservationDate
    )
    return HttpResponse("Done!!")


@api_view(['GET'])
def getReservations(request):
    res = None
    if str(list(request.query_params.keys())[0]) == "lvl":
        level = int(request.query_params.get('lvl'))
        res = Reservation.objects.all()[level * 20:(level + 1) * 20]
    elif str(list(request.query_params.keys())[0]) == "len":
        length = int(request.query_params.get('len'))
        res = Reservation.objects.all()[0:length]

    return HttpResponse(toJson(res), content_type="application/json")


@api_view(['PUT'])
def updateRes(request):
    resID = int(request.query_params.get('id'))
    PID = str(request.query_params.get('pid'))
    DID = str(request.query_params.get('did'))
    gender = str(request.query_params.get('gender'))
    reservationDate = int(request.query_params.get('date'))

    res = Reservation.objects.get(ID=resID)
    res.PID = PID
    res.DID = DID
    res.gender = gender
    res.reservations_date = reservationDate
    res.save()

    return HttpResponse("Updated!!")


@api_view(['DELETE'])
def delRes(request):
    resId = int(request.query_params.get('id'))
    doc = Reservation.objects.get(ID=resId)
    doc.delete()

    return HttpResponse("Done!!")
