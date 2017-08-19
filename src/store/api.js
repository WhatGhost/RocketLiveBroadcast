import Vue from 'vue'
import VueResource from 'vue-resource'

Vue.use(VueResource)
/**
 * This class contains some methods to connect backend.
 * @module Api
 */
/**
 * This class contains some methods to connect backend.
 * @class api
 */
export default {
    /**
    * Get data from backend.
    *
    *
    * @method get
    * @param url {Object} An `url` Object
    * @param request {Object} An 'request' Object
    * @return {Object} The result
    */
    get(url, request) {
        return Vue.http.get(url, request)
            .then((response) => Promise.resolve(response))
            .catch((error) => Promise.reject(error))
    },
    /**
    * Post data to backend.
    *
    *
    * @method post
    * @param url {Object} An `url` Object
    * @param request {Object} An 'request' Object
    * @return {Object} The result
    */
    post(url, request) {
        return Vue.http.post(url, request)
            .then((response) => Promise.resolve(response))
            .catch((error) => Promise.reject(error))
    },
    /**
    * Patch data to backend.
    *
    *
    * @method patch
    * @param url {Object} An `url` Object
    * @param request {Object} An 'request' Object
    * @return {Object} The result
    */
    patch(url, request) {
        return Vue.http.patch(url, request)
            .then((response) => Promise.resolve(response))
            .catch((error) => Promise.reject(error))
    },
    /**
    * Delete data from backend.
    *
    *
    * @method delete
    * @param url {Object} An `url` Object
    * @param request {Object} An 'request' Object
    * @return {Object} The result
    */
    delete(url, request) {
        return Vue.http.delete(url, request)
            .then((response) => Promise.resolve(response))
            .catch((error) => Promise.reject(error))
    }
}
