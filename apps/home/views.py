# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.shortcuts import render
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from custom_modules.mongo_connect import *


@login_required(login_url="/login/")
def index_four(request):
    context = {}  # {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def room(request, room_name):

    html_template = loader.get_template('home/chat.html')
    # return HttpResponse(html_template.render(context, request))
    return render(request, "chat.html", {"room_name": room_name})
#
# def home_page(request):
#    context = {'segment': 'index'}
#
#
#    return render(request,'home/index-four.html')


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        if load_template == "lstm.html" :
            
            result = mong_cl.get_data_from_any(
            query={}, name_of_data_base='django_data', name_of_table='predictions_made')
            result['predictions_30_mins']['dates_trans']=  result['timestamps_30_mins'][0]
            
            result['predictions_30_mins']['preds']=result['predictions_30_mins'][0]
            ready_outbound=result['predictions_30_mins'].join(result['timestamps_30_mins'], lsuffix='preds_', rsuffix='times_')
        
            #result['predictions_30_mins']['predictions']=result['predictions_30_mins'].values

            print("this is the \n ",ready_outbound.head())# ['predictions_30_mins'].T.to_json(orient="records"))
            json_load=result['predictions_30_mins'].to_json(orient="records")
            
            # Pass the data to the template
            context = { 'predictions_30_mins' :  json_load }

            #print(context)

            return render(request, 'home/lstm.html', context)

        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except Exception as e :
        print(e.args)
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def chat_window(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    print("logging errors")
    html_template = loader.get_template('home/' + 'chat_window.html')
    return HttpResponse(html_template.render(context, request))
