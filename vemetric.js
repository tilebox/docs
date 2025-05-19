window.vmtrcq = window.vmtrcq || [];
window.vmtrc = window.vmtrc || function () {
    window.vmtrcq.push(Array.prototype.slice.call(arguments))
};

const script = document.createElement('script');
script.src = 'https://cdn.vemetric.com/main.js';
script.defer = true;
script.setAttribute('data-token', 'rQI52fw6s6frnSOR');
document.head.appendChild(script);
