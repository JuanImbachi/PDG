const path = 'http://127.0.0.1:8000'

import axios from 'axios'

function getCases () {
  return axios.get(`${path}/api/dengueCases/`)
}

function deleteCase(id) {
  return axios.delete(`${path}/api/dengueCases/${id}/`)
}

export default{
  getCases,
  deleteCase,
}
