// src/api/losApi.ts

import axios from "axios";
import type { LengthOfStayRequest } from "../models/LengthOfStayRequest";

const api = axios.create({
    baseURL: "http://localhost:8000"
});

export const predictLOS = async (
    request: LengthOfStayRequest
) => {

    const response = await api.post(
        "/los/predict",
        request
    );

    return response.data;
};