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



export default{
  getCases,
  postCreateCase,
  deleteCase,
  path
}
