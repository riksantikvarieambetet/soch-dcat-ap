import os
import configparser
import io
import requests
from lxml import etree


config = configparser.ConfigParser()
config.read('config.ini')


if 'SOCH_API_KEY' in os.environ:
    soch_api_key = os.environ.get('SOCH_API_KEY')
else:
    soch_api_key = config['DEFAULT']['soch_api_key']

service_index_source = 'http://www.kulturarvsdata.se/ksamsok/api?method=getServiceOrganization&value=all&x-api=' + soch_api_key

r = requests.get(service_index_source)
xml = etree.XML(r.content)

institutions = list()
services = list()

for institution_node in xml.xpath('/result/institution'):
    institution = {}
    institution['name_sv'] = institution_node.xpath('.//namnswe')[0].text or ''
    institution['name_en'] = institution_node.xpath('.//namneng')[0].text or ''
    institution['webpage'] = institution_node.xpath('.//websida')[0].text or ''
    institution['contact_email'] = institution_node.xpath('.//epostkontaktperson')[0].text or ''

    if institution['webpage'] == '':
        del institution
        continue

    institutions.append(institution)

    for service_node in institution_node.xpath('.//services/service'):
        service = {}
        service['title'] = service_node.xpath('.//namn')[0].text or ''
        service['description'] = service_node.xpath('.//beskrvning')[0].text or ''
        service['contact_email'] = institution['contact_email']
        service['publisher_url'] = institution['webpage']

        if service['description'] == '':
            del service
            continue

        services.append(service)
        del service

    del institution

agent_template_file = open('source/agent-template.xml', 'r')
agent_template = agent_template_file.read()
agent_template_file.close()

dataset_template_file = open('source/dataset-template.xml', 'r')
dataset_template = dataset_template_file.read()
dataset_template_file.close()

root_template_file = open('source/root-template.rdf', 'r')
root_template = root_template_file.read()
root_template_file.close()

agents_output = ''
datasets_output = ''

for agent in institutions:
    agents_output += agent_template.replace('{ webpage }', agent['webpage']).replace('{ email }', agent['contact_email']).replace('{ name_en }', agent['name_en']).replace('{ name_sv }', agent['name_sv'])



for dataset in services:
    datasets_output += dataset_template.replace('{ description }', dataset['description']).replace('{ publisher }', dataset['publisher_url']).replace('{ title }', dataset['title']).replace('{ email }', dataset['contact_email'])

final_data = root_template.replace('{ datasets }', datasets_output).replace('{ agents }', agents_output)

os.makedirs(os.path.dirname('output/soch.rdf'), exist_ok=True)
with open('output/soch.rdf', 'w', encoding='utf-8') as f:
    f.write(final_data)

print('DONE')
