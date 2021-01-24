import axios from 'axios'
import { TokenService } from '../src/storage/service'

//const path = 'http://127.0.0.1:8000'
const path = 'https://pdgmaps.rj.r.appspot.com'
const apiMapKey = '[INSERT YOUR API KEY]'

function auth (email, password){
  return axios.post(`${path}/auth/`, {
    username: email,
    password: password,
 })
}
function getCases () {
  return axios.get(`${path}/api/dengueCases/`)
}

function postCreateCase (newRegister) {
  let axiosConfig = {
    headers: {
      'Authorization': 'Token '+ TokenService.getToken()
    }
  }

  return  axios.post(`${path}/api/dengueCases/`, newRegister, axiosConfig)
}

function deleteCase(id) {
  let axiosConfig = {
    headers: {
      'Authorization': 'Token '+ TokenService.getToken()
    }
  }
  return axios.delete(`${path}/api/dengueCases/${id}/`, axiosConfig)
}

function updateCSV() {
  return axios.get(`${path}/api/updateCSV/`)
}

function getCasesByCity(body){

  return axios({
    method: 'post',
    url: `${path}/api/cases/`,
    headers: {},
    data: body
  })
}

function getNeighborhoodsByCity (city_searched) {
  return axios.get(`${path}/api/neighborhoods/${city_searched}/`)
}

function getNeighborhoodsToPredict (city_searched) {
  return axios.get(`${path}/api/neighborhoods/predict/${city_searched}/`)
}

function getPrediction(body){
  return axios({
    method: 'post',
    url: `${path}/api/prediction/`,
    headers: {},
    data: body
  })
}

function getCasesByCityNeighborhood(body){

    return axios({
    method: 'post',
    url: `${path}/api/datesChart/`,
    headers: {},
    data: body
  })
}

function getCasesCountByCityNeighborhoodYear(body){
  return axios({
    method: 'post',
    url: `${path}/api/casesCount/`,
    headers: {},
    data: body
  })
}

function getLocation(neighborhood,city){
  return axios.get(`https://maps.googleapis.com/maps/api/geocode/json?&address=${city},${neighborhood},Colombia&key=${apiMapKey}`)
}

export default{
  auth,
  getCases,
  getCasesByCity,
  getNeighborhoodsByCity,
  getCasesByCityNeighborhood,
  getCasesCountByCityNeighborhoodYear,
  getLocation,
  postCreateCase,
  deleteCase,
  getNeighborhoodsToPredict,
  getPrediction,
  path,
  updateCSV
}
