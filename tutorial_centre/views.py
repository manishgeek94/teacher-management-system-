from django.shortcuts import render, HttpResponse
from django.views.generic import View
from tutorial_centre.models import Student, Teacher
from django.core.serializers import serialize
import json
from .forms import StudentForm, TeacherForm
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import time
import requests
from django.http import Http404


@method_decorator(csrf_exempt, name='dispatch')
class Student_data(View):
    def get(self, request, *args, **kwargs):
        """This API helps to get all records defined in the table"""
        empty_list = []
        student_info = Student.objects.all()
        for entry in student_info:
            empty_list.append([entry])
        if len(empty_list) < 1:
            return HttpResponse(json.dumps({'msg': 'No item found', 'time': time.time()}, indent=4))

        else:
            # json_data = serialize('json', student_info)
            # teacher_info = Teacher.objects.all()
            a = []
            for i in student_info.iterator():
                p_data = [
                    {
                        "student_name": i.student_name,
                        "id": i.student_id,
                        "user_name": i.student_name,
                        "teacher_alloted": i.teacher_alloted,
                    }
                ]
                a.append(p_data)

            print(a)
            # p_data = json.loads(json_data)
            final_list = []
            for obj in a:
                #     student_bio = obj['fields']
                final_list.append(obj)
            # # print(final_list)

            json_data = json.dumps(final_list, indent=4)
            return HttpResponse(json_data, content_type='application/json')


@method_decorator(csrf_exempt, name='dispatch')
class Teacher_update_id(View):
    def get_object_by_id(self, id):
        try:
            techie_info = Teacher.objects.get(teacher_id=id)
        except Teacher.DoesNotExist:
            techie_info = None
        return techie_info

    def put(self, request, id, *args, **kwargs):
        teach = self.get_object_by_id(id)

        if teach is None:
            json_data = json.dumps({'msg': 'No match found during updation'})
            return HttpResponse(json_data)
        data = request.body
        provided_data = json.loads(data)
        original_data = {

            'teacher_name': teach.teacher_name,
            'teacher_subjects': teach.teacher_name,
        }

        original_data.update(provided_data)
        # for k,v in provided_data.items():
        #     original_data[k]=v
        form = TeacherForm(original_data, instance=teach)
        if form.is_valid():
            form.save(commit=True)
            json_data = json.dumps({'msg': 'message updated successfully'})
            return HttpResponse(json_data, content_type='application/json')
        if form.errors:
            json_data = json.dumps(form.errors)
            return HttpResponse(json_data, content_type='application/json')

    def delete(self, request, id, *args, **kwargs):
        """Deletes the User by there ID whenever required"""
        techie = self.get_object_by_id(id)

        if techie is None:
            json_data = json.dumps({'msg': 'No match found to delete'})
            return HttpResponse(json_data, status=404)

        status, deleted_item = techie.delete()

        if status == 1:
            json_data = json.dumps({'msg': 'Record get deleted permanently'})
            return HttpResponse(json_data, status=404)

        json_data = json.dumps({'msg': 'Something went wrong,try again'})
        return HttpResponse(json_data, status=404)
