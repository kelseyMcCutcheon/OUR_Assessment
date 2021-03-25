import React, { Component } from 'react';
import {useState, useEffect} from 'react';
import { readString } from 'papaparse';
import $ from 'jquery';
import './NumberSense.css';
import axios from 'axios';
import "./NumberSenseQuestions.csv" as Questions;


function NumberSense(){
  return() {
    return <div>Data</div>
  }
}

export default NumberSense;
