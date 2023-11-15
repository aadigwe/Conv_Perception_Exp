import numpy as np
import pandas as pd
import csv
import os

def load_fields(fpath,input_type='text',phone_list_path=''):
    lines = [l.strip() for l in open(fpath, encoding='utf-8')]
    if fpath.endswith('.tsv'):
        columns = lines[0].split('\t')
        fields = list(zip(*[t.split('\t') for t in lines[1:]]))
    return {c:f for c, f in zip(columns, fields)}

#phrases = load_fields('/Users/adaezeadigwe/Desktop/Edinburgh/Projects/Conv_Perception_Exp/sentences.tsv')
styletext = '<style>table {width:100%;}table, th, td {border: 1px solid black;border-collapse: collapse;}</style>'
output_directory= "./output/results_new"

def html_start_syntax():
    html_file = open('index.html', 'w')
    # Title
    html_file.write('<!DOCTYPE html><html>'+styletext +
                '<body><h1>Controllable TTS Samples</h1><h6>Sample Sentences from Switchbpard and Persuasion for Good Corpus</h6>')
    return html_file

def html_end_syntax(html_file):
    html_file.write('</body></html>')
    html_file.close()


def build_utt_control_dictionary(utt, output_directory):
    utt_synthesis_dictionary = {}
    for folderitem in os.listdir(output_directory):
        print(folderitem)
        _, pa, pr, _ = folderitem.split('~')
        for fn in os.listdir(os.path.join(output_directory, folderitem)):
            if fn.endswith('wav') and fn.startswith(utt):
                audiofullpath=os.path.join(output_directory, folderitem, fn)
                key = pa+'|'+pr
                utt_synthesis_dictionary[key] = audiofullpath

    return utt_synthesis_dictionary


utterance_ids = [
    '001',
    '002',
    '2019-16',
    '3389-90',
    '17510',
    '9026',
    '14417'
]

pa = ['pa-0.5', 'pa0',  'pa0.5', 'pa0.8']
pr = ['pr-0.5','pr0',  'pr0.5', 'pr0.8']

#HTML Start File
html_file = html_start_syntax()

for utt in utterance_ids:
    utt_synthesis_dictionary = build_utt_control_dictionary(utt, output_directory)
    available_comb_pairs = utt_synthesis_dictionary.keys()

    
    
    html_file.write('<h4>'+utt+'</h4>')
    #Write First Row
    html_file.write('<table><tr>''<th>''</th>')
    for pa_value in pa:
        html_file.write('<th>'+pa_value+'</th>')
    html_file.write('</tr>')
    
    for pr_ctrl_val in pr:
        html_file.write('<tr><td>'+pr_ctrl_val+'</td>')
        for pa_ctrl_val in pa:
            key_comb = pa_ctrl_val+'|'+pr_ctrl_val
            if key_comb in available_comb_pairs:
                print(utt_synthesis_dictionary[key_comb])
                html_file.write('<td><audio controls><source src='+'"' +
                        utt_synthesis_dictionary[key_comb] + '"' + ' type="audio/mpeg"></audio></td>')
            else:
                html_file.write('<td>N/A</td>')
        html_file.write('</tr>')
    html_file.write('</table>')


    #input()

#End of HTML
html_end_syntax(html_file)
