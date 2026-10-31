
import React,{useState} from 'react';

import LOSForm from "../components/LOSForm";

import PredictionResult from '../components/PredictionResult';

export default function PredictionPage(){
 const [response,setResponse]=useState<any>(null);
 return <div style={{maxWidth:1200,margin:'20px auto',fontFamily:'Segoe UI'}}>
 <h1>Hospital Length of Stay Prediction</h1>
 <LOSForm onResult={setResponse}/>
 <PredictionResult response={response}/>
 </div>
}
