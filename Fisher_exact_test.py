#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 10:00:24 2020

@author: rezvan
"""

import scipy.stats as stats
import csv

with open(f'/Volumes/GoogleDrive/.../Phase 2/Fisher counts.csv', mode='r') as original_file:
        csv_reader = csv.DictReader(original_file)
        
        with open(f'fisher_test.csv', mode='a') as file:
            file_writer = csv.writer(file, delimiter=',')
            file_writer.writerow(['Heuristic', 'Presence of guidelines', 'Intention revealing names', 'Use of comments' ,'Use of descriptions', 'Duplicate code', 'Dead code', 'presence of test cases'])
            
            for row in csv_reader:
                
                ratio_guideline, pvalue_guideline = stats.fisher_exact([[row["Presence of guidelines1"], row["Presence of guidelines2"]], [row["Presence of guidelines3"], row["Presence of guidelines4"]]])
                ratio_names, pvalue_name = stats.fisher_exact([[row["Intention revealing names1"], row["Intention revealing names2"]], [row["Intention revealing names3"], row["Intention revealing names4"]]])
                ratio_comments, pvalue_comments = stats.fisher_exact([[row["Use of comments1"], row["Use of comments2"]], [row["Use of comments3"], row["Use of comments4"]]])
                ratio_description, pvalue_description = stats.fisher_exact([[row["Use of descriptions1"], row["Use of descriptions2"]], [row["Use of descriptions3"], row["Use of descriptions4"]]])
                ratio_duplicate, pvalue_duplicate = stats.fisher_exact([[row["Duplicate code1"], row["Duplicate code2"]], [row["Duplicate code3"], row["Duplicate code4"]]])
                ratio_dead, pvalue_dead = stats.fisher_exact([[row["Dead code1"], row["Dead code2"]], [row["Dead code3"], row["Dead code4"]]])
                ratio_test, pvalue_test = stats.fisher_exact([[row["presence of test cases1"], row["presence of test cases2"]], [row["presence of test cases3"], row["presence of test cases4"]]])
                
                file_writer.writerow([row["Heuristic"], pvalue_guideline, pvalue_name, pvalue_comments, pvalue_description, pvalue_duplicate, pvalue_dead, pvalue_test])
                
        file.close(); 

