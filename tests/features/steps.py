# -*- coding: utf-8 -*-
from lettuce import step, world
from calculadora import Calculadora


@step(u'cuando realizo la operación')
def cuando_realizo_la_operacion(step):
    pass

@step(u'Dado que ingreso los numeros "([^"]*)" y "([^"]*)"')
def dado_que_ingreso_los_numeros_group1_y_group2(step, num1, num2):
    world.cal = Calculadora()
    world.cal.suma(int(num1), int(num2))
@step(u'entonces obtengo el resultado "([^"]*)"')
def entonces_obtengo_el_resultado_group1(step, esperado):
	obtenido = world.cal.obtener_resultado()
	assert int(esperado) == obtenido,'El resultado esperado de '+esperado+" y el obtenido es "+str(obtenido)

@step(u'Dado que resto los numeros "([^"]*)" y "([^"]*)"')
def dado_que_resto_los_numeros_group1_y_group2(step, num1, num2):
    world.cal = Calculadora()
    world.cal.resta(int(num1), int(num2))

@step(u'Dado que multiplico los numeros "([^"]*)" y "([^"]*)"')
def dado_que_multiplico_los_numeros_group1_y_group2(step, num1, num2):
    world.cal = Calculadora()
    world.cal.multiplicacion(int(num1), int(num2))

@step(u'Dado que divido los numeros "([^"]*)" y "([^"]*)"')
def dado_que_divido_los_numeros_group1_y_group2(step, num1, num2):
    world.cal = Calculadora()
    world.cal.division(int(num1), int(num2))

@step(u'Dado que potencio el numero "([^"]*)" a la "([^"]*)"')
def dado_que_potencio_el_numero_group1_a_la_group2(step, num1, num2):
    world.cal = Calculadora()
    world.cal.potencia(int(num1), int(num2))

@step(u'Dado que saco la raiz del numero "([^"]*)"')
def dado_que_saco_la_raiz_del_numero_group1(step, num1):
    world.cal = Calculadora()
    world.cal.raiz2(int(num1))