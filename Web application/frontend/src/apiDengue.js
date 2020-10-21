import axios from 'axios'
import { TokenService } from '../src/storage/service'

const path = 'http://127.0.0.1:8000'

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
  console.log(id, axiosConfig)
  return axios.delete(`${path}/api/dengueCases/${id}/`, axiosConfig)
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

function getCasesByCityNeighborhood(body){

  return axios({
    method: 'post',
    url: `${path}/api/datesChart/`,
    headers: {},
    data: body
  })
}

export default{
  getCases,
  getCasesByCity,
  getNeighborhoodsByCity,
  getCasesByCityNeighborhood,
  postCreateCase,
  deleteCase,
  path
}
